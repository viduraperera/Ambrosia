from django.db import models
from datetime import *
from datetime import datetime

# Create your models here.
# Create your models here.


class Employee(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    MARITALSTATUS = (
        ('Marr', 'Married'),
        ('UnMarr', 'Unmarried'),
    )
    EMPLOYEETYPE = (
        ('Pay', 'Permanent'),
        ('Temp', 'Temparory'),
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
    EMPGROUP = (
        ('staf', 'Staff'),
        ('facwork', 'FactoryWorker'),
    )
    DESIGNATION = (
        ('FO', 'Factory_Officer'),
        ('AFO', 'AssistantFactory_Officer'),
        ('CLR', 'Clerk'),
        ('TRA', 'Trainee'),

    )
    epfNo = models.IntegerField(null=True)
    empGroup = models.CharField(max_length=50, choices=EMPGROUP)
    designation = models.CharField(max_length=50, choices=DESIGNATION)
    nic = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)


class attendance(models.Model):
    DAYTYPE = (
        ('FD', 'FullDay'),
        ('HD', 'HalfDay'),
    )
    STATUS = (
        ('Pres', 'Present'),
        ('Abs', 'Absent'),
    )
    date = models.DateField(null=True, blank=True)
    daytype = models.CharField(max_length=20, choices=DAYTYPE)
    attendaceStatus = models.CharField(max_length=50, choices=STATUS)
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)


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



