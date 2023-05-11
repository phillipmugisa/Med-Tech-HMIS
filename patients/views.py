from django.shortcuts import render
from django.views import View

from patients import models as PatientModals
from manager import models as ManagerModels
from doctor import models as DoctorModels

import os

class PatientView(View):
    template_name = "patients/index.html"
    context_data = {
        "view_name" : f"{os.environ.get('APPLICATION_NAME')} - Patients",
        "doctor_specialities" : DoctorModels.DoctorSpeciality.objects.all(),
        "visit_categories" : ManagerModels.VisitCategory.objects.all(),
        # "doctors" : [
        #     {
        #         "doctor" : doctor,
        #         "speciality" : doctor.speciality.all().first()
        #     } for doctor in DoctorModels.Doctor.objects.all()
        # ]
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)
        
class VisitsView(View):
    template_name = "patients/visits.html"
    context_data = {
        "view_name" : f"{os.environ.get('APPLICATION_NAME')} - Visits",
        "doctor_specialities" : DoctorModels.DoctorSpeciality.objects.all(),
        "visit_categories" : ManagerModels.VisitCategory.objects.all(),
        # "doctors" : [
        #     {
        #         "doctor" : doctor,
        #         "speciality" : doctor.speciality.all().first()
        #     } for doctor in DoctorModels.Doctor.objects.all()
        # ]
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)

class TriageView(View):
    template_name = "patients/triage.html"
    context_data = {
        "view_name" : f"{os.environ.get('APPLICATION_NAME')} - Visits"
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)