from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import *
from datetime import datetime

# Create your models here.

#--------------------------------------------------------------------------------------------------------------

#Tea Gerades Model - Ravija
class TeaGrades(models.Model):
    teaGrade = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table ='tea_grade'

    def __str__(self):
        return self.teaGrade

#-------------------------------------------------------------------------------------------------------------

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
