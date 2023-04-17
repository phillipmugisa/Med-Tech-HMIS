from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# python
import os
import uuid
import string
import datetime

# from patients.models import Patient

class Person(models.Model):
    class Meta:
        abstract = True

    GenderChoices = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    firstname = models.CharField(_("First Name"), max_length=256, null=False, blank=False)
    middlename = models.CharField(_("Middle Name"), max_length=256, null=True, blank=True)
    lastname = models.CharField(_("Last Name"), max_length=256, null=False, blank=False)
    age = models.IntegerField(_("Age"), default=0, null=True, blank=True)
    date_of_birth = models.DateTimeField(_("Date of Birth"), null=True, blank=True)
    nin = models.CharField(_("National Identification Number"), max_length=256, null=False, blank=False)
    gender = models.CharField(_("Gender"), max_length=256, choices=GenderChoices, null=False, blank=False)
    telnumber = models.CharField(_("Phone Number"), max_length=256, null=False, blank=False)
    alttelnumber = models.CharField(_("Alternative Phone Number"), max_length=256, null=True, blank=True)
    email = models.EmailField(_("Email"), null=True, blank=True)
    address = models.CharField(_("Address"), max_length=256, null=True, blank=True)
    slug = models.SlugField(
        _("Safe Url"), unique=True, blank=True, null=True, max_length=200
    )
    
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()
        if not self.slug:
            self.slug = slugify(f"{self.getFullName()}{uuid.uuid4()}")[:200]
        
        if not self.date_of_birth and self.age:
            birth_year = datetime.datetime.now().year - self.age
            dob = datetime.datetime(birth_year, 1, 1)
            self.date_of_birth = dob.strftime("%Y-%m-%d")
            
        elif not self.age and self.date_of_birth:
            dob = datetime.datetime.strptime(dob, self.date_of_birth)
            self.age = (datetime.datetime.now() - dob).days // 365

        super().save(*args, **kwargs)

    def getFullName(self):
        if self.middlename:
            return f"{self.firstname} {self.middlename} {self.lastname}"
        return f"{self.firstname} {self.lastname}"

    def __str__(self) -> str:
        return f"{self.getFullName()}"
    
class DoctorSpeciality(models.Model):
    name = models.CharField(_("Name"), max_length=256, null=False, blank=False)
    def __str__(self) -> str:
        return f"{self.name}"

class Doctor(Person):
    speciality = models.ManyToManyField(to=DoctorSpeciality, related_name="doctor_speciality")
    