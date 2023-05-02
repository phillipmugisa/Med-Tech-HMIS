from django.urls import path
from doctor import views as DoctorViews

app_name = "doctor"

urlpatterns = [
    path("", DoctorViews.DoctorHomeView.as_view(), name="doctor-home")
]