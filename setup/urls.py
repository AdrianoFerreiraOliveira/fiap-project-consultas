from django.contrib import admin
from django.urls import path, include
from RestConsulta.views import medicos

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('medicos/', medicos),
    path("__reload__/", include("django_browser_reload.urls")),
]
