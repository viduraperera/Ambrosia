from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
from datetime import *

# Create your models here.
from Ambrosia_Project.validators import nic_validator


#-----Employee Management Malka--------------------------------------------------------------------------


class Employee(models.Model):
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
    )
    MARITALSTATUS=(
        ('Married','Married'),
        ('UnMarried','Unmarried'),
    )
    EMPLOYEETYPE=(
        ('Permanent','Permanent'),
        ('Temparory','Temparory'),
    )
    EMPGROUP = (
        ('staff', 'Staff'),
        ('factory_Worker', 'FactoryWorker'),
    )
    DESIGNATION = (
        ('Factory_Officer', 'Factory_Officer'),
        ('AssistantFactory_Officer', 'AssistantFactory_Officer'),
        ('Clerk', 'Clerk'),
        ('Trainee', 'Trainee'),
        ('Supervisor', 'Supervisor'),
        ('Cashier', 'Cashier'),
        ('Driver','Driver'),
    )

    nic = models.CharField(max_length=12, unique=True, validators=[nic_validator])
    epfNo = models.IntegerField(unique=True, null=True, validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='EPF No can only contain numbers',
            code='EPF No is invalid'
        )
    ])
    empImage = models.ImageField(null=True, blank=True, upload_to="images/")
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=50, choices=GENDER)
    dob = models.DateField(null=True)
    maritalStatus = models.CharField(max_length=50, choices=MARITALSTATUS)
    contactNo = models.CharField(max_length=10, null=True, validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='Contact No can only contain numbers',
            code='Invalid Contact No '
        ),
        RegexValidator(
            regex='^.{10}$',
            message='Contact No length is invalid',
            code='Invalid Contact No ',
        )
    ])
    doa = models.DateField(null=True)
    basicSalary = models.FloatField(null=True)
    empType = models.CharField(max_length=50, choices=EMPLOYEETYPE,null=True)
    empGroup = models.CharField(max_length=50, choices=EMPGROUP, null=True)
    designation = models.CharField(max_length=50, choices=DESIGNATION,null=True, blank=True)



class attendance(models.Model):
    DAYTYPE = (
        ('FD', 'FullDay'),
        ('HD', 'HalfDay'),
    )
    STATUS = (
        ('Pres', 'Present'),
        ('Abs', 'Absent'),
    )
    date = models.DateField(blank=True)
    daytype = models.CharField(max_length=20, choices=DAYTYPE, blank=True)
    attendaceStatus = models.CharField(max_length=50, choices=STATUS, blank=True)
    empID = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="attendance", null=True
    )

    class Meta:
        unique_together = (('date', 'empID'),)
