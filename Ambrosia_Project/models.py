from django.db import models
from datetime import datetime
from datetime import *
from datetime import datetime

# Create your models here.
# Create your models here.


class Broker(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'Broker'

# class Buyer(models.Model):
#     vat_regno = models.CharField(max_length=30)
#     name = models.CharField(max_length=50)

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






    class Meta:
        db_table = 'Buyer'

class Auction_Stock(models.Model):

    StatusGroup = [
        ('S', 'Sold'),
        ('N', 'NotSold'),
        ('P', 'Pending'),
    ]

    invoice = models.IntegerField(null=True);
    net_weight = models.FloatField()
    total_weight = models.FloatField()
    no_of_packets = models.IntegerField()
    status = models.CharField(max_length=10, choices=StatusGroup)
    sold_count = models.IntegerField()
    price = models.FloatField()

    class Meta:
        db_table = 'Auction_Stock'


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


class TeaGrades(models.Model):
    teaGrade = models.CharField(max_length=10)
    class Meta:
        db_table ='tea_grade'

class Tea_add_prod(models.Model):
    date = models.DateField()
    total_weight = models.FloatField()
    tea_grades=models.ForeignKey(TeaGrades, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'add_product'


class packetType(models.Model):
    packet_weight_id = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)

    class Meta:
        db_table = 'packetType'

class teaCategory(models.Model):
    category_id = models.CharField(max_length=10)
    description = models.CharField(max_length=10)

    class Meta:
        db_table = 'teaCategory'

class categoryProduct(models.Model):
    cp_id = models.CharField(max_length=10)
    price = models.FloatField()
    category_id = models.ForeignKey(teaCategory, on_delete=models.CASCADE, null=True)
    packet_weight_id = models.ForeignKey(packetType, on_delete=models.CASCADE, null=True)

class preorder(models.Model):
    preorder_level = models.CharField(max_length=10)
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)

class Accumulate(models.Model):
    noOf_Packets = models.IntegerField()
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)

class Packet_stock(models.Model):
    product_ID = models.CharField(max_length=10)
    no_ofPackets = models.IntegerField()
    date = models.DateField()
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)

class Sales_Transactions(models.Model):
    noOfPackets = models.IntegerField()
    total_Price = models.FloatField()
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)
    product_ID = models.ForeignKey(Packet_stock, on_delete=models.CASCADE, null=True)


class Funds(models.Model):
    date = models.DateField(default=datetime.now)
    emp_etf = models.FloatField()
    epf_employee = models.FloatField()
    epf_employer = models.FloatField()

    class Meta:
        db_table = "funds"


class Allowance(models.Model):
    allowance_by_price = models.FloatField()
    incentive_1 = models.FloatField()
    incentive_2 = models.FloatField()

    class Meta:
        db_table = "allowance"



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


