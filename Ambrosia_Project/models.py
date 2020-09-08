from django.db import models

# Create your models here.
# Create your models here.
class Broker(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'Broker'

# class Buyer(models.Model):
#     vat_regno = models.CharField(max_length=30)
#     name = models.CharField(max_length=50)