from django.db import models
from django.conf import settings
from facility.models import Dorm
from decimal import Decimal

# Create your models here.
class Account(models.Model):
    dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE)
    institution = models.CharField(max_length=64)
    treasurer = models.ManyToManyField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=64)
    iban = models.CharField(max_length=34)
    bic = models.CharField(max_length=11)

    def __str__(self):
        return self.dorm.short + "_" + self.institution
