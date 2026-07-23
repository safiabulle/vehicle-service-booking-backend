from django.db import models

from appointments.models import Appointment


class Payment(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PAID = "PAID", "Paid"
        FAILED = "FAILED", "Failed"

    class Method(models.TextChoices):
        MPESA = "MPESA", "M-Pesa"
        CARD = "CARD", "Card"
        CASH = "CASH", "Cash"

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="payment",
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(
    max_length=20,
    choices=Method.choices,
    blank=True,
    )

    payment_status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    transaction_reference = models.CharField(
    max_length=100,
    blank=True,
    )

    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.transaction_reference} - "
            f"{self.payment_status}"
        )
