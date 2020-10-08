from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from Ambrosia_Project.forms import FundFrom, Allowance, AllowanceForm
from Ambrosia_Project.models import *
from Ambrosia_Project.salary_calculations import  *


# ---------------------------start of funds of employee-----------------------------------

@login_required(login_url='login')
def emp_fund_view(request):
    # check funds table
    fund_obj = Funds.objects.first()
    if fund_obj is None:
        fund = FundFrom()
        fund_obj = fund.save(commit=False)
        fund_obj.emp_etf = 3
        fund_obj.epf_employee = 8
        fund_obj.epf_employer = 12

        fund_obj.save()

    funds = Funds.objects.all()
    return render(request, "funds_table.html", {'funds': funds})


@login_required(login_url='login')
def emp_funds_add(request):
    form = FundFrom()

    if request.method == 'POST':
        form = FundFrom(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('emp_fund_view')
            except:
                pass
    var = {'forms': form}
    return render(request, 'add_funds.html', var)


@login_required(login_url='login')
def emp_funds_delete(request, id):
    funds = Funds.objects.get(pk=id)
    funds.delete()
    return redirect('emp_fund_view')


@login_required(login_url='login')
def emp_funds_edit(request, id):
    fund_edit = Funds.objects.get(pk=id)

    form = FundFrom(instance=fund_edit)

    var = {'fundForm': form, 'Fid': id}
    return render(request, 'edit_funds.html', var)


@login_required(login_url='login')
def emp_funds_update(request, id):
    funds_update = Funds.objects.get(pk=id)

    funds_2 = FundFrom(request.POST, instance=funds_update)

    if funds_2.is_valid():
        funds_2.save()
        messages.success(request, 'Record Updated Successfully')
        var = {'funds_update': funds_update}

        return redirect('emp_fund_view')


# ---------------------------end of funds of employee-----------------------------------

# ---------------------------start of allowance of employee-----------------------------------


@login_required(login_url='login')
def emp_allowance(request):
    allowance = Allowance.objects.all()
    return render(request, "allowance.html", {'allowance': allowance})


@login_required(login_url='login')
def emp_allowance_add(request):
    allowance = AllowanceForm()
    if request.method == 'POST':
        allowance = AllowanceForm(request.POST)
        if allowance.is_valid():
            try:
                allowance.save()
                return redirect('emp_allowance')
            except:
                pass
    var = {'allowance': allowance}
    return render(request, 'add_allowance.html', var)


@login_required(login_url='login')
def emp_allowance_edit(request, id):
    allowance_edit = Allowance.objects.get(pk=id)

    form = AllowanceForm(instance=allowance_edit)

    var = {'allowanceForm': form, 'Fid': id}
    return render(request, 'edit_allowance.html', var)


@login_required(login_url='login')
def emp_allowance_update(request, id):
    allowance_update = Allowance.objects.get(pk=id)
    allowance = AllowanceForm(request.POST, instance=allowance_update)

    if allowance.is_valid():
        allowance.save()
        messages.success(request, 'Record Updated Successfully')
        var = {'allowance_update': allowance_update}

        return redirect('emp_allowance')


@login_required(login_url='login')
def emp_allowance_delete(request, id):
    allowance = Allowance.objects.get(pk=id)
    allowance.delete()
    return redirect('emp_allowance')

# ---------------------------end of allowance of employee-----------------------------------


@login_required(login_url='login')
def emp_salary_main(request):
    employee = Employee.objects.all()
    return render(request, 'employee_salary.html', {'employee': employee})


@login_required(login_url='login')
def emp_etf_view(request):
    return render(request, 'etf_table_view.html')


@login_required(login_url='login')
def emp_epf_view(request):
    return render(request, 'epf_table_view.html')


@login_required(login_url='login')
def emp_salary_single_view(request):

    if request.method == "POST":
        year = request.POST.get("year")
        month = request.POST.get("month")
        emp_id = request.POST.get("e_id")
         # validate year and month

        if year is None and month is None:
            emp_employee = Employee.objects.get(id=emp_id)
            return render(request, 'emp_salary_single_view.html', {'emp_employee': emp_employee})

        else:
            emp_employee = Employee.objects.get(id=emp_id)
            all_cals = salary_cal(year, month, emp_id)
            var = {
                'emp_employee': emp_employee,
                'all_cals': all_cals,
                'year': year,
                'month': month,
            }

            return render(request, 'emp_salary_single_view.html', var)


@login_required(login_url='login')
def emp_add_salary_view(request):

    if request.method == "POST":
        year = request.POST.get("year")
        month = request.POST.get("month")
        employee_id = request.POST.get("employee_id")

        salary_obj = EmployeeSalary.objects.filter(emp_id=employee_id, year=year, month=month)

        if len(salary_obj) < 1:

            basic_salary = request.POST.get("basic_salary")
            monthly_attendance = request.POST.get("monthly_attendance")
            monthly_basic_salary_for_month = request.POST.get("monthly_basic_salary_for_month")
            monthly_etf_month = request.POST.get("monthly_etf_month")
            monthly_epf_employee_month = request.POST.get("monthly_epf_employee_month")
            monthly_epf_employer_month = request.POST.get("monthly_epf_employer_month")

            salary = EmployeeSalary()
            salary.year = year
            salary.month = month
            salary.emp_id = employee_id
            salary.basic_salary_of_day = basic_salary
            salary.attendance_on_month = monthly_attendance
            salary.basic_salary_of_month = monthly_basic_salary_for_month
            salary.etf_of_month = monthly_etf_month
            salary.epf_employee_month = monthly_epf_employee_month
            salary.epf_employer_month = monthly_epf_employer_month

            salary.save()
            return redirect('emp_salary_main')

        else:
            messages.error(request, "this employee salary already calculated")
            return redirect('emp_salary_main')

    return None


@login_required(login_url='login')
def emp_final_salary_view(request):

    emp_salary = EmployeeSalary.objects.all()
    emp_all = Employee.objects.all()
    var = {
        'emp_salary': emp_salary,
        'emp_all': emp_all,
    }
    return render(request, 'final_salary.html', var)


@login_required(login_url='login')
def emp_final_salary_single_view(request):

    if request.method == 'POST':
        emp_salary_id = request.POST.get("s_id")

        emp_allowance_id = request.POST.get("allowance_id")

        if emp_allowance_id is not None:

            emp_advance = request.POST.get("advance")
            emp_tea_advance = request.POST.get("tea_advance")
            emp_loan = request.POST.get("loan")
            emp_ot_hours = request.POST.get("ot_hours")

            details = {
                'emp_salary_id': emp_salary_id,
                'emp_advance': emp_advance,
                'emp_tea_advance': emp_tea_advance,
                'emp_ot_hours': emp_ot_hours,
                'emp_loan': emp_loan,
                'emp_allowance_id': emp_allowance_id,
            }

            final_calculation = calcuate_final(details)

            emp_salary = EmployeeSalary.objects.get(id=emp_salary_id)
            allowance = Allowance.objects.all()
            var = {
                'emp_salary': emp_salary,
                'allowance': allowance,
                'final_calculation': final_calculation,
            }

            return render(request, 'final_salary_single_view.html', var)

        emp_salary = EmployeeSalary.objects.get(id=emp_salary_id)
        allowance = Allowance.objects.all()

        var = {
            'emp_salary': emp_salary,
            'allowance': allowance,
        }

    return render(request, 'final_salary_single_view.html', var)


@login_required(login_url='login')
def emp_final_total_salary_view(request):

    if request.method == "POST":
        salary_id = request.POST.get("s_id")
        employee_salary = request.POST.get("total_salary")
        salary_record = EmployeeSalary.objects.get(id=salary_id)

        chk_all_b_price = salary_record.allowance_b_price

        if chk_all_b_price is None:

            final_salary = float(employee_salary) - salary_record.epf_employee_month

            salary_record.allowance_b_price = request.POST.get("all_b_price")
            salary_record.incentive_1 = request.POST.get("incen_1")
            salary_record.incentive_2 = request.POST.get("incen_2")
            salary_record.ot_hours = request.POST.get("employee_ot_hours")
            salary_record.ot_amount_for_month = request.POST.get("ot_amount")
            salary_record.loan = request.POST.get("employee_loan")
            salary_record.advance = request.POST.get("employee_advance")
            salary_record.tea_advance = request.POST.get("employee_tea_advance")
            salary_record.total_deduction = request.POST.get("total_deduction")
            salary_record.total_salary = employee_salary
            salary_record.remaining_salary = final_salary

            salary_record.save()
            return redirect('emp_final_salary_view')

        else:
            messages.error(request, "this employee salary already calculated")
            return redirect('emp_final_salary_view')

    return None

@login_required(login_url='login')
def delete_total_salary(request):

    if request.method == "POST":
        salary_id = request.POST.get("salary_id")
        salary = EmployeeSalary.objects.get(id=salary_id)

        salary.delete()

        return redirect('emp_final_salary_view')
