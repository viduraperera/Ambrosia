from datetime import datetime

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm, Textarea


# Create your models here.
# Create your models here.


#This class is for registration form
class Registration(models.Model):
    Sup_Name = models.CharField(max_length=50)
    nicNo = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=100, null=True)
    DOB = models.DateField()
    Reg_Date = models.DateField(default=datetime.now)
    est_name = models.CharField(max_length=50)
    ROUTE = (
        ('WE', "WE"),
        ('BR', "BR"),
        ('BNR', "BNR"),
    )
    route = models.CharField(max_length=3, choices=ROUTE)
    SUP_SCALE = (
        ('sm', 'Small-Scale'),
        ('lg', 'Large-Scale'),
    )
    sup_scale = models.CharField(max_length=2, choices=SUP_SCALE)
    PAY_TYPE = (
        ('C', 'Cash'),
        ('CH', 'Check'),
        ('BD', 'Bank-Deposit'),
    )
    pay_Type = models.CharField(max_length=3, choices=PAY_TYPE)
    acc_No = models.CharField(max_length=20, null=True, validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='ERROR!!',
            code='Acc No is Not Valid!'
        )
    ])
    bank = models.CharField(max_length=50)

    class Meta:
        db_table = "ambrosia_project_register"

    def __int__(self):
        return self.id


class LeafStock(models.Model):
    weight = models.FloatField()
    rec_Date = models.DateField(default=datetime.now)
    rec_Time = models.TimeField(default=datetime.now)
    supplier = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "ambrosia_project_leafstock"

    #def __int__(self):
     #   return self.supplier_id


class Payment(models.Model):
    additions = models.FloatField()
    pay_Date = models.DateField(default=datetime.now)
    pay_Time = models.TimeField(default=datetime.now)
    advances = models.FloatField()
    transport_costs = models.FloatField()
    other_costs = models.FloatField()
    tot_weight = models.FloatField()
    per_kilo_price = models.FloatField()
    supplier = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "ambrosia_project_payment"
        
    #def __int__(self):
     #   return self.supplier_id




