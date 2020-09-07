from django.db import models
from datetime import datetime

# Create your models here.
# Create your models here.


class Broker(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=10, null=True)


class Buyer(models.Model):
    vat_regno = models.CharField(max_length=30)
    name = models.CharField(max_length=50)


class Funds(models.Model):
    date = models.DateField(default=datetime.now)
    emp_epf = models.FloatField()
    etf_employee = models.FloatField()
    etf_employer = models.FloatField()


class Meta:
    db_table = "funds"
