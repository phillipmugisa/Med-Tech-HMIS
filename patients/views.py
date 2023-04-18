from django.shortcuts import render
from django.views import View

from patients import models as PatientModals
from manager import models as ManagerModels

APPLICATION_NAME = "MedSafe Health Management Information System"

class PatientView(View):
    template_name = "patients/index.html"
    context_data = {
        "view_name" : f"{APPLICATION_NAME} - Patients",
        "doctor_specialities" : ManagerModels.DoctorSpeciality.objects.all(),
        "doctors" : [
            {
                "doctor" : doctor,
                "speciality" : doctor.speciality.all().first()
            } for doctor in ManagerModels.Doctor.objects.all()
        ]
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)
        
class VisitsView(View):
    template_name = "patients/visits.html"
    context_data = {
        "view_name" : f"{APPLICATION_NAME} - Visits",
        "doctor_specialities" : ManagerModels.DoctorSpeciality.objects.all(),
        "doctors" : [
            {
                "doctor" : doctor,
                "speciality" : doctor.speciality.all().first()
            } for doctor in ManagerModels.Doctor.objects.all()
        ]
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)

class TriageView(View):
    template_name = "patients/triage.html"
    context_data = {
        "view_name" : f"{APPLICATION_NAME} - Visits"
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)