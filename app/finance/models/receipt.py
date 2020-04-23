from django.db import models

# Create your models here.
class Receipt(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="receipt_name",max_length=64)
    document = models.FileField(verbose_name="receipt_document", upload_to='receipts/')
    