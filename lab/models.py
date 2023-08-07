from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import datetime

from patients import models as PatientModals
from manager import models as ManagerModels
from doctor import models as DoctorModels

class TestCategory(models.Model):
    name = models.CharField(_("Name"), max_length=256, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"{self.name}"

class LabTest(models.Model):
    class Meta:
        ordering = ("-id","-updated_on")

    name = models.CharField(_("Name"), max_length=256, null=False, blank=False)
    description = models.TextField(_("Description"), null=True, blank=True)
    dafault_range = models.TextField(_("Default Range"), null=True, blank=True)
    category = models.ForeignKey(to=TestCategory, on_delete=models.CASCADE, related_name="test_category")
    price = models.DecimalField(_("Price"), decimal_places=3, max_digits=9, null=True, blank=True)
    currency = models.CharField(_("Currency"), max_length=5, default="UGX")
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
    has_subtest = models.BooleanField(_("Has Sub Test"), default=False)

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()
        super().save(*args, **kwargs)

class SubTest(models.Model):
    test = models.ForeignKey(to=LabTest, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=256, null=False, blank=False)
    dafault_range = models.TextField(_("Default Range"), null=True, blank=True)

class RequestCategory(models.Model):
    name = models.CharField(_("Name"), max_length=256, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"{self.name}"

class Request(models.Model):
    class Meta:
        ordering = ("-id","-updated_on")

    visit = models.ForeignKey(to=PatientModals.Visit, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(to=RequestCategory, on_delete=models.CASCADE, related_name="request_category", null=True, blank=True)
    doctor = models.ForeignKey(to=DoctorModels.Doctor, on_delete=models.CASCADE, related_name="doctor", null=True, blank=True)
    attendant = models.ForeignKey(to=DoctorModels.Doctor, on_delete=models.CASCADE, related_name="attendant", null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
    handled = models.BooleanField(_("Handled"), default=False)
    
    def __str__(self) -> str:
        return f"{self.visit}"

    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()
        super().save(*args, **kwargs)

class AssignedTest(models.Model):
    class Meta:
        ordering = ("-id","-updated_on")

    request = models.ForeignKey(to=Request, on_delete=models.CASCADE, null=True)
    test = models.ForeignKey(to=LabTest, on_delete=models.CASCADE)
    price = models.DecimalField(_("Price"), decimal_places=3, max_digits=9, null=True, blank=True)
    naration = models.TextField(_("Naration"), null=True, blank=True)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
        
    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()
    
        if not self.price:
            self.price = self.test.price
        super().save(*args, **kwargs)

class TestResult(models.Model):
    class Meta:
        ordering = ("-id","-updated_on")

    test = models.ForeignKey(to=AssignedTest, on_delete=models.CASCADE)
    results = models.TextField(_("Test Results"), null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
        
    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.test.name}"

class SubTestResult(models.Model):
    class Meta:
        ordering = ("-id","-updated_on")

    subtest = models.ForeignKey(to=SubTest, on_delete=models.CASCADE)
    results = models.DecimalField(_("Result"), decimal_places=3, max_digits=6, null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)
        
    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.test.name}"