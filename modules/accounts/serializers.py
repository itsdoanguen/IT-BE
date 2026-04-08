from rest_framework import serializers

from modules.accounts.models import NguoiDung


class NguoiDungSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = NguoiDung
        fields = ["id", "email", "password", "vai_tro", "tao_luc"]
        read_only_fields = ["id", "tao_luc"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        return NguoiDung.objects.create_user(password=password, **validated_data)
