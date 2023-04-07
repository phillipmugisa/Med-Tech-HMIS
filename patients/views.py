from django.shortcuts import render
from django.views import View

APPLICATION_NAME = "MedSafe Health Management Information System"

class PatientView(View):
    template_name = "patients/index.html"
    context_data = {
        "view_name" : f"{APPLICATION_NAME} - Patients"
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)
        
class VisitsView(View):
    template_name = "patients/index.html"
    context_data = {
        "view_name" : f"{APPLICATION_NAME} - Visits"
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context_data)