from django.contrib import admin
from django.urls import path, include
from RestConsulta.views import MedicosViewSet, PacientesViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("api-medicos", MedicosViewSet, basename="Medicos")
router.register("api-pacientes", PacientesViewSet, basename="Pacientes")

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
