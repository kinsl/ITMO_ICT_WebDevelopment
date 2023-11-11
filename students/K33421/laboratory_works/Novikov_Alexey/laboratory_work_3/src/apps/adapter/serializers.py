from rest_framework import serializers

from apps.adapter.models import Adapter


class AdapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adapter
        fields = ["id", "full_name"]

    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.last_name} {obj.first_name}"
