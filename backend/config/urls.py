from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/vehicles/", include("vehicles.urls")),
    path("api/services/", include("services.urls")),
    path("api/appointments/", include("appointments.urls")),
    path("api/payments/", include("payments.urls")),
]