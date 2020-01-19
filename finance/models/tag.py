from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(verbose_name="transaction_tag_name",max_length=64)
    