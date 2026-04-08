from rest_framework import serializers

from modules.profiles.models import HoSoCongTy, HoSoUngVien


class HoSoUngVienSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoSoUngVien
        fields = "__all__"


class HoSoCongTySerializer(serializers.ModelSerializer):
    class Meta:
        model = HoSoCongTy
        fields = "__all__"
