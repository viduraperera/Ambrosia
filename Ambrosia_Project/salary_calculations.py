from Ambrosia_Project.models import *


def salary_cal(year, month, emp_id):

    # retrive emp id

    basic_salary = Employee.objects.get(emp_id).basicSalary
