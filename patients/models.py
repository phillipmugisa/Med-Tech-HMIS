from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# python
import os
import uuid
import string

from manager import models as ManagerModels

class Patient(ManagerModels.Person):
    patient_id = models.CharField(_("relationship"), max_length=256, null=True, blank=True)

    def generatePatientId(self):
        hospital_abbr = ""
        for word in os.environ.get("HOSPITAL_NAME").split(" "):
            hospital_abbr = hospital_abbr + word[0].upper()

        patient_id = f"{hospital_abbr}{uuid.uuid4()}"[:8]

        # chech if id exists
        if Patient.objects.filter(patient_id=patient_id):
            patient_id = f"{hospital_abbr}{uuid.uuid4()}"[:8]

        return patient_id

    def save(self, *args, **kwargs):
        if not self.patient_id:
            self.patient_id = self.generatePatientId()

        super(Patient, self).save(*args, **kwargs)

class NextOfKin(ManagerModels.Person):
    relationship = models.CharField(_("relationship"), max_length=256, null=False, blank=False)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, related_name="next_of_kin", null=True, blank=True)

class Visit(models.Model):
    patient = models.OneToOneField(to=Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(to=ManagerModels.Doctor, on_delete=models.SET_NULL, null=True)
    speciality = models.ForeignKey(to=ManagerModels.DoctorSpeciality, on_delete=models.SET_NULL, null=True)
    updated_on = models.DateField(_("Updated on"), null=True, blank=True)
    created_on = models.DateField(_("Created on"), default=timezone.now)

    def __str__(self) -> str:
        return f"{self.patient}"


    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()

        super().save(*args, **kwargs)
