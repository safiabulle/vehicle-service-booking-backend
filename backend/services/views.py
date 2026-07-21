from rest_framework import generics, permissions
from accounts.permissions import IsAdminOrReadOnly
from .models import Service, ServiceCategory
from .serializers import (
    ServiceSerializer,
    ServiceCategorySerializer,
)


class ServiceCategoryListView(generics.ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]