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
        
        hospital_abbr = hospital_abbr + "/P"

        today = datetime.datetime.now()

        patient_id = f"{hospital_abbr}/{str(today.year)[2:]}/{str(today.month)}/{str(today.day)}/{str(today.hour)}{str(today.minute)}{str(today.second)}"

        # check if id exists
        if Patient.objects.filter(patient_id=patient_id):
            # if exists. regenerate
            patient_id = f"{hospital_abbr}/{str(today.year)[2:]}/{str(today.month)}/{str(today.day)}/{str(today.hour)}{str(today.minute)}{str(today.second)}"

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
    visit_id = models.CharField(_("Visit Id"), max_length=256, null=True, blank=True)
    doctor = models.ForeignKey(to=DoctorModels.Doctor, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(to=ManagerModels.VisitCategory, on_delete=models.CASCADE)
    speciality = models.ForeignKey(to=DoctorModels.DoctorSpeciality, on_delete=models.SET_NULL, null=True)
    billing = models.OneToOneField(to=FinanceModels.Billing, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(_("Completed"), default=False)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    visit_date = models.DateTimeField(_("Date"), default=timezone.now)

    def generateVisitId(self):
        hospital_abbr = ""
        for word in os.environ.get("HOSPITAL_NAME").split(" "):
            hospital_abbr = hospital_abbr + word[0].upper()

        hospital_abbr = hospital_abbr + "/V"

        today = datetime.datetime.now()

        visit_id = f"{hospital_abbr}/{str(today.year)[2:]}/{str(today.month)}/{str(today.day)}/{str(today.hour)}{str(today.minute)}{str(today.second)}"

        # check if id exists
        if Visit.objects.filter(visit_id=visit_id):
            # if exists. regenerate
            visit_id = f"{hospital_abbr}/{str(today.year)[2:]}/{str(today.month)}/{str(today.day)}/{str(today.hour)}{str(today.minute)}{str(today.second)}"

        return visit_id

    def __str__(self) -> str:
        return f"{self.patient} - {self.visit_id}"


    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()
        if not self.visit_id:
            self.visit_id = self.generateVisitId()

        super().save(*args, **kwargs)

class Triage(models.Model):
    class Meta:
        ordering = ("-id","-updated_on")
        
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
    class Meta:
        ordering = ("-id","-updated_on")
        
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=256, null=True, blank=True)
    comment = models.TextField(_("Doctor's Comments"), null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"

class GeneralFinding(models.Model):
    class Meta:
        ordering = ("-id","-updated_on")
        
    visit = models.ForeignKey(to=Visit, on_delete=models.CASCADE)
    presenting_complaints = models.CharField(_("presenting complaints"), max_length=256, null=True, blank=True)
    clinical_notes = models.CharField(_("clinical notes"), max_length=256, null=True, blank=True)
    rohs = models.CharField(_("rohs"), max_length=256, null=True, blank=True)
    psh = models.CharField(_("psh"), max_length=256, null=True, blank=True)
    poh = models.CharField(_("poh"), max_length=256, null=True, blank=True)
    cvs = models.CharField(_("cvs"), max_length=256, null=True, blank=True)
    general_appearance = models.CharField(_("general appearance"), max_length=256, null=True, blank=True)
    respiratory = models.CharField(_("respiratory"), max_length=256, null=True, blank=True)
    ent = models.CharField(_("ent"), max_length=256, null=True, blank=True)
    abdomen_and_Gut = models.CharField(_("abdomen and Gut"), max_length=256, null=True, blank=True)
    cns = models.CharField(_("cns"), max_length=256, null=True, blank=True)
    eye = models.CharField(_("eye"), max_length=256, null=True, blank=True)
    muscular_skeletal = models.CharField(_("muscular skeletal"), max_length=256, null=True, blank=True)
    skin = models.CharField(_("skin"), max_length=256, null=True, blank=True)
    pv_pr = models.CharField(_("pv/pr"), max_length=256, null=True, blank=True)
    psychological_status = models.CharField(_("psychological status"), max_length=256, null=True, blank=True)
    provisional_status = models.CharField(_("provisional status"), max_length=256, null=True, blank=True)
    treatment_plan = models.CharField(_("treatment plan"), max_length=256, null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()

        super().save(*args, **kwargs)

class PaedeatricNote(models.Model):
    class Meta:
        ordering = ("-id","-updated_on")
        
    visit = models.ForeignKey(to=Visit, on_delete=models.CASCADE)
    notes = models.CharField(_("notes"), max_length=256, null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()

        super().save(*args, **kwargs)

class GynNote(models.Model):
    class Meta:
        ordering = ("-id","-updated_on")
        
    visit = models.ForeignKey(to=Visit, on_delete=models.CASCADE)
    notes = models.CharField(_("notes"), max_length=256, null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()

        super().save(*args, **kwargs)