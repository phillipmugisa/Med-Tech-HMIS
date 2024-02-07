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
    
    path("allergy/", AppApiViews.AllergyListView.as_view(), name='allergy_list'),
    path("allergy/<int:pk>", AppApiViews.AllergyRetrieveView.as_view(), name='allergy_retrieve'),
    path("allergy/<int:pk>/update/", AppApiViews.AllergyUpdateView.as_view(), name='allergy_update'),
    path("allergy/create/", AppApiViews.AllergyCreateView.as_view(), name='allergy_create'),
    path("allergy/<str:patient_id>/patient/", AppApiViews.PatientAllergyListView.as_view(), name='patients_allergy_list'),
    
    path("generalfindings/", AppApiViews.GeneralFindingsListView.as_view(), name='general_findings_list'),
    path("generalfindings/<int:pk>", AppApiViews.GeneralFindingsRetrieveView.as_view(), name='general_findings_retrieve'),
    path("generalfindings/<int:pk>/update/", AppApiViews.GeneralFindingsUpdateView.as_view(), name='general_findings_update'),
    path("generalfindings/create/", AppApiViews.GeneralFindingsCreateView.as_view(), name='general_findings_create'),
    path("generalfindings/<str:patient_id>/patient/", AppApiViews.PatientGeneralFindingsListView.as_view(), name='patients_general_findings_list'),
    path("generalfindings/<str:visit_id>/visit/", AppApiViews.VisitGeneralFindingsListView.as_view(), name='visit_general_findings_list'),
    
    path("paedeatricnotes/", AppApiViews.PaedeatricsNotesListView.as_view(), name='paedeatrics_list'),
    path("paedeatricnotes/<int:pk>", AppApiViews.PaedeatricsNotesRetrieveView.as_view(), name='paedeatrics_retrieve'),
    path("paedeatricnotes/<int:pk>/update/", AppApiViews.PaedeatricsNotesUpdateView.as_view(), name='paedeatrics_update'),
    path("paedeatricnotes/create/", AppApiViews.PaedeatricsNotesCreateView.as_view(), name='paedeatrics_create'),
    path("paedeatricnotes/<str:patient_id>/patient/", AppApiViews.PatientPaedeatricsNotesListView.as_view(), name='patients_paedeatrics_list'),
    path("paedeatricnotes/<str:visit_id>/visit/", AppApiViews.VisitPaedeatricsNotesListView.as_view(), name='visit_paedeatrics_list'),
    
    path("gynnotes/", AppApiViews.GynNotesListView.as_view(), name='gyn_notes_list'),
    path("gynnotes/<int:pk>", AppApiViews.GynNotesRetrieveView.as_view(), name='gyn_notes_retrieve'),
    path("gynnotes/<int:pk>/update/", AppApiViews.GynNotesUpdateView.as_view(), name='gyn_notes_update'),
    path("gynnotes/create/", AppApiViews.GynNotesCreateView.as_view(), name='gyn_notes_create'),
    path("gynnotes/<str:patient_id>/patient/", AppApiViews.PatientGynNotesListView.as_view(), name='patients_gyn_notes_list'),
    path("gynnotes/<str:visit_id>/visit/", AppApiViews.VisitGynNotesListView.as_view(), name='visit_gyn_notes_list'),


    # lab    
    path("lab/requests/", AppApiViews.LabRequestListView.as_view(), name='lab_requests_list'),
    path("lab/requests/<int:pk>", AppApiViews.LabRequestRetrieveView.as_view(), name='lab_requests_retrieve'),
    path("lab/requests/<int:pk>/update/", AppApiViews.LabRequestUpdateView.as_view(), name='lab_requests_update'),
    path("lab/requests/create/", AppApiViews.LabRequestCreateView.as_view(), name='lab_requests_create'),
    path("lab/requests/<str:patient_id>/patient/", AppApiViews.PatientLabRequestListView.as_view(), name='patient_lab_requests_list'),
    path("lab/requests/<int:pk>/visit/", AppApiViews.VisitLabRequestListView.as_view(), name='visit_lab_requests_list'),
    path("lab/requests/<str:category>//", AppApiViews.CategoryLabRequestListView.as_view(), name='category_lab_requests_list'),
    
    path("lab/tests/", AppApiViews.LabTestListView.as_view(), name='lab_tests_list'),
    path("lab/tests/<int:pk>", AppApiViews.LabTestRetrieveView.as_view(), name='lab_tests_retrieve'),
    path("lab/tests/<int:pk>/update/", AppApiViews.LabTestUpdateView.as_view(), name='lab_tests_update'),
    path("lab/tests/create/", AppApiViews.LabTestCreateView.as_view(), name='lab_tests_create'),
    path("lab/tests/<int:pk>/request/", AppApiViews.RequestLabTestListView.as_view(), name='request_lab_tests_list'),
    path("lab/tests/<str:category>/", AppApiViews.CategoryLabTestListView.as_view(), name='category_lab_tests_list'),
]