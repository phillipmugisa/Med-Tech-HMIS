from django.shortcuts import render
from django.views import View

import os

class DoctorHomeView(View):
    template_name = "doctor/index.html"
    context_data = {
        "view_name" : f"{os.environ.get('APPLICATION_NAME')} - Doctor",
        # "doctor_specialities" : ManagerModels.DoctorSpeciality.objects.all(),
        # "doctors" : [
        #     {
        #         "doctor" : doctor,
        #         "speciality" : doctor.speciality.all().first()
        #     } for doctor in ManagerModels.Doctor.objects.all()
        # ]
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)

