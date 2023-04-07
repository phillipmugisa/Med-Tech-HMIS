from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("patients.urls", namespace="patients")),
    path('admin/', admin.site.urls),
]
