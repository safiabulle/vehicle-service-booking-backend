from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(
        source="customer.username",
        read_only=True,
    )

    vehicle_registration = serializers.CharField(
        source="vehicle.registration_number",
        read_only=True,
    )

    service_name = serializers.CharField(
        source="service.name",
        read_only=True,
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "customer",
            "customer_name",
            "vehicle",
            "vehicle_registration",
            "service",
            "service_name",
            "appointment_date",
            "appointment_time",
            "status",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = (
            "id",
            "customer",
            "customer_name",
            "created_at",
            "updated_at",
        )