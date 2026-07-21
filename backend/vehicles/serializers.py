from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "owner",
            "make",
            "model",
            "year",
            "registration_number",
            "color",
            "vin",
            "created_at",
            "updated_at",
        ]
        read_only_fields = (
            "id",
            "owner",
            "created_at",
            "updated_at",
        )