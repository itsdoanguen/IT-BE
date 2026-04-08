from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from modules.accounts.models import NguoiDung
from modules.accounts.serializers import NguoiDungSerializer


class NguoiDungViewSet(viewsets.ModelViewSet):
	queryset = NguoiDung.objects.all().order_by("id")
	serializer_class = NguoiDungSerializer

	def get_permissions(self):
		if self.action == "create":
			return [AllowAny()]
		return [IsAuthenticated()]
