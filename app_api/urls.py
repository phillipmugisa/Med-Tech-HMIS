from django.urls import path
from app_api import views as AppApiViews

app_name = "app_api"

urlpatterns = [
    path("patients/", AppApiViews.PatientListView.as_view(), name='patient_list'),
    path("patients/create/", AppApiViews.PatientCreateView.as_view(), name='patient_create'),
    path("patients/<str:patient_id>/", AppApiViews.PatientRetrieveView.as_view(), name='patients_retrieve'),
    path("patients/<str:patient_id>/update/", AppApiViews.PatientUpdateView.as_view(), name='patient_update'),

    path("nextOfKin/<int:pk>/", AppApiViews.NextOfKinRetrieveView.as_view(), name='nok_list'),
    path("nextOfKin/<int:pk>/update/", AppApiViews.NextOfKinUpdateView.as_view(), name='nok_update'),
    path("patients/create/nextOfKin/", AppApiViews.PatientNokCreateView.as_view(), name='patient_create_nok'),
    
    path("visits/", AppApiViews.VisitsListView.as_view(), name='visit_list'),
    path("visits/<int:pk>", AppApiViews.VisitsRetrieveView.as_view(), name='visit_retrieve'),
    path("visits/<int:pk>/update", AppApiViews.VisitsUpdateView.as_view(), name='visit_update'),
    path("visits/create/", AppApiViews.VisitCreateView.as_view(), name='visit_create'),
]