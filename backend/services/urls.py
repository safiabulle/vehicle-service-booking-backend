from django.urls import path

from .views import (
    ServiceCategoryListView,
    ServiceListCreateView,
    ServiceDetailView,
)

urlpatterns = [
    path("categories/", ServiceCategoryListView.as_view(), name="service-categories"),
    path("", ServiceListCreateView.as_view(), name="service-list"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="service-detail"),
]