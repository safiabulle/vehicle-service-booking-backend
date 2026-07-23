from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    appointment_customer = serializers.CharField(
        source="appointment.customer.username",
        read_only=True,
    )

    service_name = serializers.CharField(
        source="appointment.service.name",
        read_only=True,
    )

    vehicle_registration = serializers.CharField(
        source="appointment.vehicle.registration_number",
        read_only=True,
    )

    appointment_date = serializers.DateField(
        source="appointment.appointment_date",
        read_only=True,
    )

    class Meta:
        model = Payment
        fields = [
            "id",
            "appointment",
            "appointment_customer",
            "service_name",
            "vehicle_registration",
            "appointment_date",
            "amount",
            "payment_method",
            "payment_status",
            "transaction_reference",
            "payment_date",
        ]
        read_only_fields = (
        "id",
        "payment_date",
        "appointment_customer",
        "service_name",
        "vehicle_registration",
        "appointment_date",
    )