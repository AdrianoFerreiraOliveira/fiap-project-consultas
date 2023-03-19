from django.contrib import admin
from django.urls import path, include
from consultasapp.views import medicos

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('medicos/', medicos),
]
