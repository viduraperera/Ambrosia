from Ambrosia_Project.models import *


def salary_cal(year, month, emp_id):
    full_day_count = 0
    half_day_count = 0
    total_attendance = 0
    basic_salary_for_month = 0
    etf_month = 0
    epf_employee_month = 0
    epf_employer_month = 0

    # retrive emp id

    basic_salary = Employee.objects.get(id=emp_id).basicSalary

    # monthly attendence calculations

    monthly_attendence = attendance.objects.filter(empID=emp_id, date__month=month, date__year=year, attendaceStatus='Present')

    for att in monthly_attendence:

        if att.daytype == 'FullDay':

            full_day_count = full_day_count + 1

        if att.daytype == 'HalfDay':

            half_day_count = half_day_count + 0.5

    total_attendance = half_day_count + full_day_count

    basic_salary_for_month = total_attendance * basic_salary

    funds = Funds.objects.first()

    emp = Employee.objects.get(id=emp_id)

    if emp.empType == "Permanent":
        etf_month = basic_salary_for_month * (funds.emp_etf / 100)
        epf_employee_month = basic_salary_for_month * (funds.epf_employee / 100)
        epf_employer_month = basic_salary_for_month * (funds.epf_employer / 100)

    static_cals = {

        'total_attendance': total_attendance,
        'basic_salary_for_month': basic_salary_for_month,
        'etf_month': etf_month,
        'epf_employee_month': epf_employee_month,
        'epf_employer_month': epf_employer_month,

    }
    return static_cals


def calcuate_final(details):

    all_id = details["emp_allowance_id"]
    employee_loan = details["emp_loan"]
    employee_ot_hours = details["emp_ot_hours"]
    employee_tea_advance = details["emp_tea_advance"]
    employee_advance = details["emp_advance"]
    salary_id = details["emp_salary_id"]

    # print(salary_id, employee_loan)

    allowance_obj = Allowance.objects.get(id=all_id)
    salary_obj = EmployeeSalary.objects.get(id=salary_id)

    attendance = salary_obj.attendance_on_month

    all_b_price = attendance * allowance_obj.allowance_by_price
    incen_1 = attendance * allowance_obj.incentive_1
    incen_2 = attendance * allowance_obj.incentive_2

    ot_amount = int(employee_ot_hours) * (salary_obj.basic_salary_of_day/9)

    total_deduction = float(employee_loan) + float(employee_tea_advance) + float(employee_advance)

    total_salary = salary_obj.basic_salary_of_month + all_b_price + incen_1 + incen_2 + ot_amount - total_deduction

    final_cal = {
        'all_b_price': all_b_price,
        'incen_1': incen_1,
        'incen_2': incen_2,

        'total_deduction': total_deduction,
        'total_salary': total_salary,

        'employee_ot_hours': employee_ot_hours,
        'ot_amount': ot_amount,
        'employee_loan': employee_loan,

        'employee_advance': employee_advance,
        'employee_tea_advance': employee_tea_advance,
    }
    return final_cal
