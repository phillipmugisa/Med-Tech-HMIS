from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# python
import os
import uuid
import string
import datetime

from manager import models as ManagerModels
from doctor import models as DoctorModels
from finance import models as FinanceModels

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

class ActiveVisitManager(models.Manager):
    def get_queryset(self):
        # Override the default queryset to exclude inactive items
        return super().get_queryset().filter(complete=False)

class Visit(models.Model):
    objects = models.Manager()
    active = ActiveVisitManager()
    class Meta:
        ordering = ("-id","-updated_on")

    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(to=DoctorModels.Doctor, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(to=ManagerModels.VisitCategory, on_delete=models.CASCADE)
    speciality = models.ForeignKey(to=DoctorModels.DoctorSpeciality, on_delete=models.SET_NULL, null=True)
    billing = models.OneToOneField(to=FinanceModels.Billing, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(_("Completed"), default=False)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    visit_date = models.DateTimeField(_("Date"), default=timezone.now)

    def __str__(self) -> str:
        return f"{self.patient}"


    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()

        super().save(*args, **kwargs)

class Triage(models.Model):
    visit = models.OneToOneField(to=Visit, on_delete=models.CASCADE)
    blood_pressure = models.DecimalField(_("Blood Pressure"), decimal_places=2, max_digits=6, null=True, blank=True)
    heart_rate = models.DecimalField(_("Heart Rate"), decimal_places=2, max_digits=6, null=True, blank=True)
    respiratory_rate = models.DecimalField(_("Respiratory Rate"), decimal_places=2, max_digits=6, null=True, blank=True)
    temperature = models.DecimalField(_("Temperature"), decimal_places=2, max_digits=6, null=True, blank=True)
    weight = models.DecimalField(_("Weight"), decimal_places=2, max_digits=6, null=True, blank=True)
    height = models.DecimalField(_("Height"), decimal_places=2, max_digits=6, null=True, blank=True)
    oxygen_saturation = models.DecimalField(_("Oxygen Saturation"), decimal_places=2, max_digits=6, null=True, blank=True)
    MUAC = models.DecimalField(_("MUAC"), decimal_places=2, max_digits=6, null=True, blank=True)
    sign_symptoms = models.TextField(_("Signs and Symptoms"), null=True, blank=True) 
    injury_details = models.TextField(_("injury Details"), null=True, blank=True) 
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.visit}"


class Allergy(models.Model):
    visit = models.OneToOneField(to=Visit, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=256, null=True, blank=True)
    comments = models.TextField(_("Doctor's Comments"), null=True, blank=True) 
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"
