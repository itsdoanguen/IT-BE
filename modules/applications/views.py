from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from modules.applications.models import UngTuyen
from modules.applications.serializers import UngTuyenSerializer


class UngTuyenViewSet(viewsets.ModelViewSet):
    queryset = UngTuyen.objects.all().order_by("-thoi_gian_ung_tuyen")
    serializer_class = UngTuyenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Nếu là ứng viên, chỉ thấy đơn của mình
        # Nếu là công ty, thấy đơn ứng tuyển vào các tin của mình
        if hasattr(user, 'vai_tro'):
            from modules.accounts.models import NguoiDung
            if user.vai_tro == NguoiDung.VaiTro.UNG_VIEN:
                return self.queryset.filter(ung_vien__ung_vien=user)
            elif user.vai_tro == NguoiDung.VaiTro.CONG_TY:
                return self.queryset.filter(tin__cong_ty__cong_ty=user)
        
        return self.queryset.none()

    @extend_schema(summary="Ứng tuyển vào một công việc")
    def create(self, request, *args, **kwargs):
        from modules.accounts.models import NguoiDung
        if request.user.vai_tro != NguoiDung.VaiTro.UNG_VIEN:
            return Response(
                {"detail": "Chỉ ứng viên mới có thể thực hiện hành động này."},
                status=status.HTTP_403_FORBIDDEN
            )
            
        # Kiểm tra xem đã được nhận việc (Accepted/Hired) ở đâu chưa
        if UngTuyen.objects.filter(
            ung_vien__ung_vien=request.user,
            trang_thai__in=[UngTuyen.TrangThai.CHAP_NHAN, UngTuyen.TrangThai.HOAN_THANH]
        ).exists():
            return Response(
                {"detail": "Bạn đã được nhận việc ở một vị trí khác và không thể ứng tuyển thêm hồ sơ mới."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        return super().create(request, *args, **kwargs)
