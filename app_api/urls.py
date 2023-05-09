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
    path("patients/<str:patient_id>/visit/", AppApiViews.PatientVisitListView.as_view(), name='patients_visit_retrieve'),
    path("visit/<int:pk>/triage/", AppApiViews.VisitTriageListView.as_view(), name='visit_triage_retrieve'),
    path("visit/<int:pk>/patient/", AppApiViews.VisitPatientListView.as_view(), name='visit_patient_retrieve'),
    
    path("triage/", AppApiViews.TriageListView.as_view(), name='triage_list'),
    path("triage/<int:pk>", AppApiViews.TriageRetrieveView.as_view(), name='triage_retrieve'),
    path("triage/<int:pk>/update/", AppApiViews.TriageUpdateView.as_view(), name='triage_update'),
    path("triage/create/", AppApiViews.TriageCreateView.as_view(), name='triage_create'),
    path("triage/<str:patient_id>/patient/", AppApiViews.PatientTriageListView.as_view(), name='patients_triage_list'),
]