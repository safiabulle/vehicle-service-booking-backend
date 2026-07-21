from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    appointment_customer = serializers.CharField(
        source="appointment.customer.username",
        read_only=True,
    )

    class Meta:
        model = Payment
        fields = [
            "id",
            "appointment",
            "appointment_customer",
            "amount",
            "payment_method",
            "payment_status",
            "transaction_reference",
            "payment_date",
        ]
        read_only_fields = (
            "id",
            "payment_date",
        )