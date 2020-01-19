from django.db import models
from facility.models import Dorm

# Create your models here.
class Room(models.Model):
    dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    level = models.CharField(max_length=8)
    