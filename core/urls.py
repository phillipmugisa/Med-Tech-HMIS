from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("patients.urls", namespace="patients")),
    path('api/', include("app_api.urls", namespace="api")),
    path('doctor/', include("doctor.urls", namespace="doctor")),
    path('dasbboard/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
