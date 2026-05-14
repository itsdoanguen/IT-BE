from rest_framework import serializers
from modules.applications.models import UngTuyen


class UngTuyenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="ung_tuyen_id", read_only=True)
    candidate_name = serializers.CharField(source="ung_vien.ho_ten", read_only=True)
    job_title = serializers.CharField(source="tin.tieu_de", read_only=True)
    company_name = serializers.CharField(source="tin.cong_ty.ten_cong_ty", read_only=True)

    class Meta:
        model = UngTuyen
        fields = ["id", "tin", "ung_vien", "trang_thai", "thoi_gian_ung_tuyen", "candidate_name", "job_title", "company_name"]
        read_only_fields = ["ung_vien", "trang_thai", "thoi_gian_ung_tuyen"]

    def validate(self, data):
        request = self.context.get("request")
        if not request or not request.user:
            raise serializers.ValidationError("Bạn cần đăng nhập để ứng tuyển.")

        # Lấy hồ sơ ứng viên của người dùng hiện tại
        from modules.profiles.models import HoSoUngVien
        try:
            hoso = HoSoUngVien.objects.get(ung_vien=request.user)
        except HoSoUngVien.DoesNotExist:
            raise serializers.ValidationError("Bạn cần cập nhật hồ sơ ứng viên trước khi ứng tuyển.")

        # Kiểm tra xem đã ứng tuyển tin này chưa
        if UngTuyen.objects.filter(tin=data["tin"], ung_vien=hoso).exists():
            raise serializers.ValidationError("Bạn đã ứng tuyển vào công việc này rồi.")

        data["ung_vien"] = hoso
        return data
