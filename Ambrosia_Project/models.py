from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import *
from datetime import datetime

# Create your models here.

#Employee Model - Malka
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


#Normal Employee Model - Malka
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


#Attendance Model  - Malka
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


#Oil Stock Model - Nethmi A
class Oil_Stock(models.Model):
    Amount = models.FloatField()
    Date = models.DateField()


#Vehicle Model - Nethmi A
class Vehicle(models.Model):
    VehicleNo = models.CharField(max_length=20)
    Status = models.BooleanField()
    NIC = models.CharField(max_length=20)
    EPF_No = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)


#Driving Records Model - Nethmi A
class Driving_Records(models.Model):
    Date = models.DateField(default= datetime.now)
    Start_Reading = models.FloatField()
    End_Reading = models.FloatField()
    VehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)


#Oil Model- Nethmi A
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


#Services Model - Nathmi A
class Services(models.Model):
    Bill_No = models.CharField(max_length=10)
    Description = models.TextField()
    Service_Date = models.DateField()
    Next_Service_Date = models.DateField()
    VehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)


#Services Model- Driver
class Driver(models.Model):
    Driver_License_No = models.CharField(max_length=10)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)


# #teacategory Model - Nethmi
class teaCategory(models.Model):
    category_id = models.CharField(max_length=10)
    description = models.CharField(max_length=10)

    class Meta:
        db_table = 'teaCategory'


#teashop products Model - Nethmi
class Tea_add_prod(models.Model):
    date = models.DateField()
    total_weight = models.FloatField()
    tea_grades=models.ForeignKey('TeaGrades', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'add_product'


#teashop packttype Model - Nethmi
class packetType(models.Model):
    packet_weight_id = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)

    class Meta:
        db_table = 'packetType'


#categoryProduct Model - Nethmi
class categoryProduct(models.Model):
    cp_id = models.CharField(max_length=10)
    price = models.FloatField()
    category_id = models.ForeignKey(teaCategory, on_delete=models.CASCADE, null=True)
    packet_weight_id = models.ForeignKey(packetType, on_delete=models.CASCADE, null=True)


#Preorder Model - Nethmi
class preorder(models.Model):
    preorder_level = models.CharField(max_length=10)
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)


#Accumlate Model - Nethmi
class Accumulate(models.Model):
    noOf_Packets = models.IntegerField()
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)


#Packet Stock Model - Nethmi
class Packet_stock(models.Model):
    product_ID = models.CharField(max_length=10)
    no_ofPackets = models.IntegerField()
    date = models.DateField()
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)


#sales transactions Model - Onella
class Sales_Transactions(models.Model):
    noOfPackets = models.IntegerField()
    total_Price = models.FloatField()
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)
    product_ID = models.ForeignKey(Packet_stock, on_delete=models.CASCADE, null=True)


#Funds model Vidura
class Funds(models.Model):
    date = models.DateField(default=datetime.now)
    emp_etf = models.FloatField()
    epf_employee = models.FloatField()
    epf_employer = models.FloatField()

    class Meta:
        db_table = "funds"


#Allowance model - Vidura
class Allowance(models.Model):
    allowance_by_price = models.FloatField()
    incentive_1 = models.FloatField()
    incentive_2 = models.FloatField()

    class Meta:
        db_table = "allowance"


#Supplier Model - Tharuka
class Supplier(models.Model):
    Sup_Name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100, null=True)
    DOB = models.DateField()
    Reg_Date = models.DateField()
    phone = models.CharField(max_length=10, null=True)


#Estate Model - Tharuka
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


#Leaf Inventory Model - Ravija
class LeafInventory(models.Model):
    in_Date = models.DateField()
    in_Time = models.TimeField()
    tray_Id = models.IntegerField()
    temp = models.FloatField()
    weight = models.FloatField()
    out_Date = models.DateField()
    out_Time = models.TimeField()

    class Meta:
        db_table ='inventory'


#LeafStock Model - Ravija
class LeafStock(models.Model):
    weight = models.FloatField()
    rec_Date = models.DateField()
    rec_Time = models.TimeField()
    #supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)


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

    active = models.IntegerField(blank=True, default=1)

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
    active = models.IntegerField(blank=True, default=1)

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
    invoice = models.IntegerField(null=True)
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

    SubID = models.IntegerField(blank=True)
    Date = models.DateField(default=datetime.now , blank=True)
    Broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    total_netWeight = models.FloatField(blank=True)
    total_grossWeight = models.FloatField(blank=True)
    total_packets = models.IntegerField(blank=True)
    active = models.IntegerField(blank=True, default=1)

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
