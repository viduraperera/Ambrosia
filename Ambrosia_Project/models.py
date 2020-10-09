from django.db import models
from datetime import *
from datetime import datetime
from django.core.validators import RegexValidator, MinValueValidator


# Create your models here.

class Transactions(models.Model):
    dateTime = models.DateTimeField(default=datetime.now)
    total_Price = models.FloatField(blank=True)
    invoice_id = models.IntegerField(blank=True)


class BillItems(models.Model):
    ITemName = (
        ('BOPF', 'BOPF'),
        ('DUST 1', 'DUST 1'),
        ('DUST 2', 'DUST 2'),
        ('FGS', 'FGS'),

    )
    Weight = (
        ('1Kg', ' 1Kg'),
        ('500g', '500g'),
        ('400g', '400g'),
        ('250g', '250Kg'),
        ('200g', '200g'),

    )
    invoice_id = models.IntegerField(blank=True)
    itemname = models.CharField(max_length=10, choices=ITemName)
    weight = models.CharField(max_length=10, choices=Weight)
    itemPrice = models.FloatField(blank=True)
    price = models.FloatField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    Quantity = models.IntegerField(validators=[MinValueValidator(1)])


class Price_Table(models.Model):
    category = (
        ('BOPF', 'BOPF'),
        ('DUST 1', 'DUST 1'),
        ('DUST 2', 'DUST 2'),
        ('FGS', 'FGS'),

    )
    weight = (
        ('1Kg', ' 1Kg'),
        ('500g', '500g'),
        ('400g', '400g'),
        ('250g', '250Kg'),
        ('200g', '200g'),

    )
    category = models.CharField(max_length=10, choices=category)
    weight = models.CharField(max_length=10, choices=weight)
    price = models.FloatField(validators=[MinValueValidator(1)])

