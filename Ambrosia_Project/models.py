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


# Supplier Management -------------------------------------------------
# This class is for registration form - Supplier Management Registration
class Registration(models.Model):
    Sup_Name = models.CharField(max_length=50)
    proPic = models.ImageField(null=True, blank=True, upload_to="images/")
    nicNo = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, null=True, validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='ERROR!! Phone Number Should Contain Only Numbers',
            code='Phone Number is Not Valid!'
        ),
        RegexValidator(
            regex='^.{10}$',
            message='ERROR!! Phone Number is Invalid!',
            code='Phone Number is Not Valid!'
        )
    ])
    email = models.CharField(max_length=100, null=True)
    DOB = models.DateField()
    Reg_Date = models.DateField(default=datetime.now)
    est_name = models.CharField(max_length=50)
    ROUTE = (
        ('AT', "AT"),
        ('HG', "HG"),
        ('NW', "NW"),
        ('PP', "PP"),
        ('UG', "UG"),
        ('UP', "UP"),
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

    def __str__(self):
        return self.nicNo


class LeafStock(models.Model):
    weight = models.FloatField()
    rec_Date = models.DateField(default=datetime.now)
    rec_Time = models.TimeField(default=datetime.now)
    # supplier = models.ForeignKey(Registration, related_name="supplier", on_delete=models.CASCADE, null=True)
    nic = models.ForeignKey(
        Registration, on_delete=models.CASCADE, null=True, related_name="leaf_stock", to_field="nicNo"
    )

    class Meta:
        db_table = "ambrosia_project_leafstock"

    # def __int__(self):
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
    payment = models.FloatField(null=True, blank=True)
    # supplier = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    nic = models.ForeignKey(
        Registration, on_delete=models.CASCADE, null=True, related_name="payments", to_field="nicNo"
    )

    class Meta:
        db_table = "ambrosia_project_payment"

    # def __int__(self):
    #   return self.supplier_id


#-----Employee Management Malka--------------------------------------------------------------------------
from Ambrosia_Project.common_utills.validators import nic_validator


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


#-------Salary Management-------------------------------------------------------
class Funds(models.Model):
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


class EmployeeSalary(models.Model):
    emp_id = models.IntegerField()
    attendance_on_month = models.FloatField()
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=20)

    allowance_b_price = models.FloatField(null=True)
    incentive_1 = models.FloatField(null=True)
    incentive_2 = models.FloatField(null=True)

    basic_salary_of_day = models.FloatField()
    basic_salary_of_month = models.FloatField()

    etf_of_month = models.FloatField()
    epf_employee_month = models.FloatField()
    epf_employer_month = models.FloatField()

    ot_hours = models.IntegerField(null=True)

    loan = models.FloatField(null=True)

    advance = models.FloatField(null=True)
    tea_advance = models.FloatField(null=True)
    ot_amount_for_month = models.FloatField(null=True)

    total_salary = models.FloatField(null=True)
    total_deduction = models.FloatField(null=True)
    remaining_salary = models.FloatField(null=True)

    class Meta:
        db_table = 'Employee_salary'


class OverTime(models.Model):
    emp_id = models.IntegerField()
    data = models.DateField(default=datetime.now)
    ot_hours = models.FloatField()

    class Meta:
        db_table = 'Over_Time'


class Advance(models.Model):
    emp_id = models.IntegerField()
    date = models.DateField(default=datetime.now)
    amount = models.FloatField()

    class Meta:
        db_table = 'advance'


class TeaAdvance(models.Model):
    emp_id = models.IntegerField()
    date = models.DateField(default=datetime.now)
    amount = models.FloatField()

    class Meta:
        db_table = 'tea_advance'


class Loan(models.Model):
    emp_id = models.IntegerField()
    date_of_loan_request = models.DateField(default=datetime.now)
    amount_loan = models.FloatField()
    time_duration = models.IntegerField()
    remaining_loan_amount = models.FloatField()
    loan_status = models.IntegerField(default=0)

    class Meta:
        db_table = 'loan'


