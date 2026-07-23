from rest_framework import generics

from .models import Payment
from .serializers import PaymentSerializer
from .permissions import IsAdminOrReadOnly


class PaymentListCreateView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Payment.objects.all()

        return Payment.objects.filter(
            appointment__customer=user
        )


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Payment.objects.all()

        return Payment.objects.filter(
            appointment__customer=user
        )