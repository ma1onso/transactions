from django.db import models
from model_utils.models import TimeStampedModel

from tompany.companies.managers import CompanyManager


class Company(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )
    is_active = models.BooleanField(
        default=True
    )

    objects = CompanyManager()

    def __str__(self):
        return self.name
