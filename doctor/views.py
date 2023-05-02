from django.shortcuts import render
from django.views import View

import os

from patients import models as PatientModals
from manager import models as ManagerModels
from doctor import models as DoctorModels

class DoctorHomeView(View):
    template_name = "doctor/index.html"
    context_data = {
        "view_name" : f"{os.environ.get('APPLICATION_NAME')} - Doctor",
        "visits" : PatientModals.Visit.objects.all() #FILTER BASED ON DOCTOR
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)

