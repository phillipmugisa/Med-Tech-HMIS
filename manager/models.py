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
    nin = models.CharField(_("National Identification Number"), max_length=256, null=False, blank=False)
    gender = models.CharField(_("Gender"), max_length=256, choices=GenderChoices, null=False, blank=False)
    telnumber = models.CharField(_("Phone Number"), max_length=256, null=False, blank=False)
    alttelnumber = models.CharField(_("Alternative Phone Number"), max_length=256, null=True, blank=True)
    email = models.EmailField(_("Email"), null=True, blank=True)
    address = models.CharField(_("Address"), max_length=256, null=True, blank=True)
    slug = models.SlugField(
        _("Safe Url"), unique=True, blank=True, null=True, max_length=200
    )
    
    created_on = models.DateField(_("Created on"), default=timezone.now)
    updated_on = models.DateField(_("Updated on"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.getFullName()}{uuid.uuid4()}")[:200]
        self.updated_on = datetime.datetime.now()

        super().save(*args, **kwargs)

    def getFullName(self):
        return f"{self.firstname} {self.middlename} {self.lastname}" if self.middlename else f"{self.firstname} {self.lastname}"

    def __str__(self) -> str:
        return f"{self.getFullName}"
    
class DoctorSpeciality(models.Model):
    name = models.CharField(_("Name"), max_length=256, null=False, blank=False)
    def __str__(self) -> str:
        return f"{self.name}"

class Doctor(Person):
    speciality = models.ManyToManyField(to=DoctorSpeciality, related_name="doctor_speciality")