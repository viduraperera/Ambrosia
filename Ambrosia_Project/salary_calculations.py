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

    monthly_attendence = attendance.objects.filter(nic=emp_id, date__month=month, date__year=year, attendaceStatus='Present')

    for att in monthly_attendence:

        if att.daytype == 'FullDay':

            full_day_count = full_day_count + 1

        if att.daytype == 'HalfDay':

            half_day_count = half_day_count + 0.5

    total_attendance = half_day_count + full_day_count

    basic_salary_for_month = total_attendance * basic_salary

    funds = Funds.objects.first()

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
