import datetime
from datetime import *
from datetime import datetime
from django.core.validators import RegexValidator
from django.db import models


#transport-------------------------------------------------------------------------

class Driver(models.Model):
    licence_no = models.CharField(max_length=10)
    epfNo = models.IntegerField(null=True)

    def __str__(self):
        return self.licence_no


class Vehicle(models.Model):
    VehicleNo = models.CharField(max_length=20, unique=True)
    Driverid = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.VehicleNo


class Driving_Records(models.Model):
    Date = models.DateField(default=datetime.now)
    Start_Reading = models.CharField(max_length=20, validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='Start reading must contain only numbers',
            code='Start date is invalid'
        )
    ])

    End_Reading = models.CharField(max_length=20,validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='End reading must contain only numbers',
            code='End date is invalid'
        )
    ])
    Meter_Difference = models.IntegerField(blank=True)
    VehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)


class Services(models.Model):
    Bill_No = models.CharField(max_length=10)
    Description = models.TextField()
    Service_Date = models.DateField(default=datetime.now)
    VehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    Amount = models.FloatField()


