from rest_framework import serializers

from modules.jobs.models import TinTuyenDung


class TinTuyenDungSerializer(serializers.ModelSerializer):
    class Meta:
        model = TinTuyenDung
        fields = "__all__"
