from rest_framework import generics, permissions
import uuid

from .models import Appointment
from .serializers import AppointmentSerializer
from payments.models import Payment


class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Appointment.objects.all()

        return Appointment.objects.filter(customer=user)

    def perform_create(self, serializer):
        appointment = serializer.save(customer=self.request.user)

        Payment.objects.create(
                appointment=appointment,
                amount=appointment.service.price,
                payment_status=Payment.Status.PENDING,
        )


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Appointment.objects.all()

        return Appointment.objects.filter(customer=user)