from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import *
from datetime import datetime

# Create your models here.

#---------Models of Ravija---------------------------------------------

class LeafInventory(models.Model):

    in_Date = models.DateField()
    in_Time = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(23.59) ])
    tray_Id = models.IntegerField()
    temp = models.FloatField()
    weight = models.FloatField(validators=[MinValueValidator(0)])
    out_Date = models.DateField()
    out_Time = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(23.59) ])

    class Meta:
        db_table = 'inventory'


class TeaGrades(models.Model):
    teaGrade = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'tea_grade'

    def __str__(self):
        return self.teaGrade


class Final_product_sub(models.Model):

    subID = models.IntegerField(blank=True)
    teaGrade = models.ForeignKey(TeaGrades, on_delete=models.CASCADE)
    gradeWeight = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        db_table="Final_product_sub"


class Final_product_Main(models.Model):

    subID = models.IntegerField(blank=True)
    totalWeight = models.FloatField(blank=True, validators=[MinValueValidator(0)])
    date = models.DateField(default= datetime.now)

    class Meta:
        db_table="Final_product_Main"


#----------------------Models Sandun---------------------------------------------------------------------------------------

#Broker Model - Sandun
class Broker(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    vat_regno = models.CharField(max_length=15, null=True, blank=True, unique=True, validators=[
        RegexValidator(
            regex='^[0-9-]*$',
            message='Vat Registration Number must contain only numbers',
            code='Vat Reg.No is Invalid'
        )
    ])
    phone = models.CharField(max_length=10, unique=True, null=True, validators=[
        RegexValidator(
            regex = '^[0-9]*$',
            message = 'Phone Number must contain only numbers.',
            code = 'Phone Number is Invalid'
        ),
        RegexValidator(
            regex = '^.{10}$',
            message = 'Phone Number length is invalid',
            code = 'Phone Number is Invalid'
        )
    ])


    class Meta:
        db_table = 'Broker'

    def __str__(self):
        return self.name


#Buyer Model - Sandun
class Buyer(models.Model):
    vat_regno = models.CharField(max_length=15, null=True, blank=True, unique=True, validators=[
        RegexValidator(
            regex = '^[0-9-]*$',
            message = 'Vat Registration Number must contain only numbers',
            code = 'Vat Reg.No is Invalid'
        )
    ])
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Buyer'

    def __str__(self):
        return self.name


#Auction SubStock Model - Sandun
class Auction_SubStock(models.Model):

    packets = (
        ('DPBS', 'DPBS'),
        ('MNBS', 'MNBS')
    )

    SubID = models.IntegerField(blank=True)
    invoice = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    no_of_packets = models.IntegerField(validators=[MinValueValidator(1)])
    net_weight = models.FloatField(validators=[MinValueValidator(1)])
    total_weight = models.FloatField(validators=[MinValueValidator(1)])
    grade = models.ForeignKey(TeaGrades, to_field='teaGrade', on_delete=models.CASCADE, blank=True)
    packetType = models.CharField(max_length=10, choices=packets, blank=True)
    date_prepared = models.DateField(default=datetime.now , blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    active = models.IntegerField(blank=True, default=1)

    class Meta:
        db_table = 'Auction_SubStock'


#Auction MainStock Model - Sandun
class Auction_MainStock(models.Model):

    SubID = models.IntegerField(primary_key= True, blank=True)
    Date = models.DateField(default=datetime.now , blank=True)
    Broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    total_netWeight = models.FloatField(blank=True)
    total_grossWeight = models.FloatField(blank=True)
    total_packets = models.IntegerField(blank=True)

    class Meta:
        db_table = 'Auction_MainStock'


#Auction Sold Stock Model - Sandun
class Auction_SoldStocks(models.Model):

    MainID = models.IntegerField(blank=True)
    SubID = models.IntegerField(blank=True)
    price = models.FloatField(validators=[MinValueValidator(1)])
    total_price = models.FloatField(validators=[MinValueValidator(1)], blank=True)
    Buyer = models.ForeignKey('Buyer', on_delete = models.CASCADE, null=True, blank=True)
    sold_Date = models.DateField()
    active = models.IntegerField(blank=True, default=1)

    class Meta:
        db_table = 'Auction_SoldStock'


#Auction Not Sold Stock Model - Sandun
class Auction_NotSoldStocks(models.Model):

    MainID = models.IntegerField(blank=True)
    SubID = models.IntegerField(blank=True)
    active = models.IntegerField(blank=True, default=1)

    class Meta:
        db_table = 'Auction_NotSoldStock'


#Auction Not Sold Stock Log Model - Sandun
class Auction_NotSoldStocksLog(models.Model):

    LastUpdated = models.DateTimeField(blank=True, auto_now_add=True)
    Description = models.TextField(blank=True)

    class Meta:
        db_table = 'Auction_NotSoldStockLog'


#Auction Not Sold Stock Details Model - Sandun
class Auction_RePreparedNotSoldStocksDetails(models.Model):
    NotSoldStockID = models.IntegerField(blank=True)
    PreviousSubStockMainID = models.IntegerField(blank=True)
    NewSubStockMainID = models.IntegerField(blank=True)
    LastUpdated = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        db_table = 'Auction_NotSoldStockDetails'

class CategoryProduct(models.Model):

    cp_name = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)

    class Meta:
        unique_together = (('category', 'weight'),)

    def __str__(self):
        return self.cp_name


#----------------------Models Nethmi S-------------------------------------------------------------------------------------

class AddPackets(models.Model):

    date = models.DateField()
    noOfPackets = models.IntegerField(validators=[MinValueValidator(1)])
    categoryProductID = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)


class Stock(models.Model):
    category = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    available_stock = models.IntegerField()

    class Meta:
        unique_together = (('category', 'weight'),)


#----------------------Models Onella---------------------------------------------------------------------------------------

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


