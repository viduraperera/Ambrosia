from django.db import models
from datetime import *
from datetime import datetime
from django.core.validators import RegexValidator

# Create your models here.


#-----Employee Management Malka--------------------------------------------------------------------------
from Ambrosia_Project.validators import nic_validator


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



