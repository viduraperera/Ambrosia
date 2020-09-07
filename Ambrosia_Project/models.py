from django.db import models

# Create your models here.
# Create your models here.
class Broker(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=10, null=True)


class Buyer(models.Model):
    vat_regno = models.CharField(max_length=30)
    name = models.CharField(max_length=50)


class Supplier(models.Model):
    Sup_Name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100, null=True)
    DOB = models.DateField()
    Reg_Date = models.DateField()
    phone = models.CharField(max_length=10, null=True)


class Estate(models.Model):
    name = models.CharField(max_length=50)
    ROUTE = (
        ('WE', "Tes1"),
        ('BR', "Test2"),
        ('BNR', "Testt3"),
    )
    route = models.CharField(max_length=3, choices=ROUTE)
    SUP_SCALE = (
        ('sm', 'Small-Scale'),
        ('lg', 'Large-Scale'),
    )
    sup_scale = models.CharField(max_length=2, choices=SUP_SCALE)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)


class LeafStock(models.Model):
    weight = models.FloatField()
    rec_Date = models.DateField()
    rec_Time = models.TimeField()
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)


