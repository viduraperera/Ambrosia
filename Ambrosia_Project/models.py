from django.db import models
from datetime import datetime

# Create your models here.
# Create your models here.
class Broker(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=50, null=True)

class Buyer(models.Model):
    vat_regno = models.CharField(max_length=30)
    name = models.CharField(max_length=50)

class Employee(models.Model):
    GENDER=(
        ('M','Male'),
        ('F','Female'),
    )
    MARITALSTATUS=(
        ('Marr','Married'),
        ('UnMarr','Unmarried'),
    )
    EMPLOYEETYPE=(
        ('Pay','Permanent'),
        ('Temp','Temparory'),
    )

    nic = models.CharField(max_length=15, unique=True)
    epfNo = models.IntegerField(unique=True, null=True)
    name = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(max_length=50, choices=GENDER)
    dob = models.DateField()
    maritalStatus = models.CharField(max_length=50, choices=MARITALSTATUS)
    contactNo = models.CharField(max_length=10, null=True)
    doa = models.DateField(null=True)
    basicSalary = models.FloatField(null=True)
    empType = models.CharField(max_length=50, choices=EMPLOYEETYPE)

class NormalEmployee(models.Model):
    EMPGROUP=(
        ('staf','Staff'),
        ('facwork','FactoryWorker'),
    )
    DESIGNATION =(
        ('FO','Factory_Officer'),
        ('AFO','AssistantFactory_Officer'),
        ('CLR','Clerk'),
        ('TRA','Trainee'),


    )
    epfNo = models.IntegerField(null=True)
    empGroup = models.CharField(max_length=50, choices=EMPGROUP)
    designation = models.CharField(max_length=50, choices=DESIGNATION)
    nic = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)


class attendance(models.Model):
    DAYTYPE=(
        ('FD','FullDay'),
        ('HD','HalfDay'),
    )
    STATUS=(
        ('Pres','Present'),
        ('Abs','Absent'),
    )
    date = models.DateField(default=datetime.now)
    daytype = models.CharField(max_length=20, choices=DAYTYPE)
    attendaceStatus = models.CharField(max_length=50, choices=STATUS)
    workingDays = models.IntegerField()
    nic = models.ForeignKey(Employee, on_delete=models.CASCADE, null= True)

class Oil_Stock(models.Model):
    Amount = models.FloatField()
    Date = models.DateField()

class Vehicle(models.Model):
    VehicleNo = models.CharField(max_length=20)
    Status = models.BooleanField()
    NIC = models.CharField(max_length=20)
    EPF_No = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)


class Driving_Records(models.Model):
    Date = models.DateField(default= datetime.now)
    Start_Reading = models.FloatField()
    End_Reading = models.FloatField()
    VehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)


class Oil(models.Model):
    Container_No = models.IntegerField()
    Type = (
        ('D''Diesel'),
        ('O''Oil'),

    )
    Consumed_Amount = models.FloatField(null=True)
    Price = models.FloatField(null=True)
    VehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    Oil_Stock = models.ForeignKey(Oil_Stock, on_delete=models.CASCADE, null=True)

class Services(models.Model):
    Bill_No = models.CharField(max_length=10)
    Description = models.TextField()
    Service_Date = models.DateField()
    Next_Service_Date = models.DateField()
    VehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)

class Driver(models.Model):
    Driver_License_No = models.CharField(max_length=10)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)




