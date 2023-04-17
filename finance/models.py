from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# python
import os
import uuid
import string

class BillingType(models.Model):
    name = models.CharField(_("Name"), max_length=256, null=False, blank=False)
    is_active = models.BooleanField(_("Type is active"), default=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Billing(models.Model):
    btype = models.ForeignKey(to=BillingType, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(_("Amount"), decimal_places=3, max_digits=10)
    paid = models.BooleanField(_("Paid"), default=False)
