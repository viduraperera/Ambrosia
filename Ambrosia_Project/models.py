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
    basic_salary_of_day = models.FloatField()
    basic_salary_of_month = models.FloatField()
    etf_of_month = models.FloatField()
    epf_employee_month = models.FloatField()
    epf_employer_month = models.FloatField()
    total_salary = models.FloatField(null=True)
    remaining_salary = models.FloatField(null=True)

    class Meta:
        db_table = 'Employee_salary'



# class EmployeeSalaryView(models.Model):
#     name = models.ForeignKey(Employee, from_fields='name', on_delete=models.CASCADE, null=True)
#     epf_no = models.ForeignKey(Employee, from_fields='epfNo', on_delete=models.CASCADE, null=True)
#     working_days = models.ForeignKey(attendance, on_delete=models.CASCADE, null=True)
#
#     year_of_salary = models.DateTimeField(auto_now_add=True)
#
#     def salary_year(self):
#         return self.year_of_salary.strftime('%Y')
#
#     month_of_salary = models.DateField(auto_now_add=True)
#
#     def salary_month(self):
#         return self.month_of_salary.strftime('%B')
#
#     class Meta:
#         db_table = 'employee_salary_view'
