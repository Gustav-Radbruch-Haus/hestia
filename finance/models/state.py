from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(verbose_name="transaction_state_name",max_length=64)
    