from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Ambrosia_Project.forms import FundFrom, Allowance, AllowanceForm
from Ambrosia_Project.models import Funds


# ---------------------------start of funds of employee-----------------------------------

@login_required(login_url='login')
def emp_fund_view(request):
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
    return render(request, 'employee_salary.html')


@login_required(login_url='login')
def emp_final_salary_view(request):
    return render(request, 'final_salary.html')


@login_required(login_url='login')
def emp_etf_view(request):
    return render(request, 'etf_table_view.html')


@login_required(login_url='login')
def emp_epf_view(request):
    return render(request, 'epf_table_view.html')