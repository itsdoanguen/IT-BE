from rest_framework import viewsets

from modules.profiles.models import HoSoCongTy, HoSoUngVien
from modules.profiles.serializers import HoSoCongTySerializer, HoSoUngVienSerializer


class HoSoUngVienViewSet(viewsets.ModelViewSet):
	queryset = HoSoUngVien.objects.all()
	serializer_class = HoSoUngVienSerializer


class HoSoCongTyViewSet(viewsets.ModelViewSet):
	queryset = HoSoCongTy.objects.all()
	serializer_class = HoSoCongTySerializer
