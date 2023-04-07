from django.urls import path
from patients import views as PatientViews

app_name = "patients"

urlpatterns = [
    path("", PatientViews.PatientView.as_view(), name="patients-home"),
    path("visits/", PatientViews.VisitsView.as_view(), name="patients-visits")
]