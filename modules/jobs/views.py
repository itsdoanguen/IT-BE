from rest_framework import viewsets

from modules.jobs.models import TinTuyenDung
from modules.jobs.serializers import TinTuyenDungSerializer


class TinTuyenDungViewSet(viewsets.ModelViewSet):
	queryset = TinTuyenDung.objects.all().order_by("-tao_luc")
	serializer_class = TinTuyenDungSerializer
