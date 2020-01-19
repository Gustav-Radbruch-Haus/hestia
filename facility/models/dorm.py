from django.db import models

# Create your models here.
class Dorm(models.Model):
    name = models.CharField(max_length=128)
    short = models.CharField(max_length=16)
    internal_name = models.CharField(max_length=32)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=16)
    city = models.CharField(max_length=128)
    province = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
