from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ambrosia_Project.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Ambrosia_Project.models import *
from Ambrosia_Project.forms import *
# Create your views here.


@login_required(login_url='login')
def registration(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'User Account '+user+' Created Successfully.')
            return redirect('view_all_users')

    context = {'form': form}
    return render(request, 'AdminRegistration.html', context)


def login_user(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            un = request.POST.get('un')
            pwd = request.POST.get('pwd')

            user = authenticate(request, username=un, password=pwd)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return render(request, 'login.html')

    return render(request, 'login.html')


@login_required(login_url='login')
def home(request):

    return render(request, 'home.html')


def logout_user(request):

    logout(request)
    return redirect('login')


@login_required(login_url='login')
def view_AllUsers(request):

    array = User.objects.all();
    print(array);
    return render(request, 'ViewAllUsers.html', {'Users': array})


@login_required(login_url='login')
def factoryHomepage(request):

    return render(request, 'factoryhome.html')


@login_required(login_url='login')
def teashopHomepage (request):

    return render(request, 'teashophome.html')

@login_required(login_url='login')
def EmployeeHome (request):

    return render(request, 'EmployeeManagement.html')

@login_required(login_url='login')
def ShowUser(request):

    uname = request.POST.get("uname")

    users = User.objects.all();

    for user in users:
        if user.username == uname:
            arrUser = user
            return render(request, 'updateUser.html', {'UserDetails': arrUser})

    return render(request, 'ViewAllUsers.html')


@login_required(login_url='login')
def UpdateUser(request):

    if request.method == 'POST':
        uname = request.POST.get('un')
        pword =request.POST.get('pwd')

        if uname != None and pword != None:
            user = User.objects.get(username=uname)
            user.password = pword
            user.save();
            messages.success(request, "User Details Updated Successfully")
            return redirect('view_all_users')

        else:
            messages.error(request, "Can't Update Details.")
            return redirect('view_all_users')

    else:
        messages.error(request, "Can't Update Details.")
        return redirect('view_all_users')

    messages.error(request, "Error.Can't Update Details.")
    return redirect('view_all_users')


@login_required(login_url='login')
def DeleteUser(request):

    uname = request.POST.get('uname')

    if request.method == 'POST' and uname != None:
        user = User.objects.get(username=uname)
        user.delete()
        messages.success(request, "User Deleted Successfully")
        return redirect('view_all_users')

    else:
        messages.error(request, "Can't Delete User.")
        return redirect('view_all_users')

    # messages.error(request, "Error.Can't Delete User.")
    # return redirect('view_all_users')


def emp_fund_view(request):
    funds = Funds.objects.all()
    return render(request, "funds_table.html", {'funds': funds})


def emp_funds_add(request):
    form = FundFrom()

    if request.method == 'POST':
        form = FundFrom(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emp_fund_view')
            except:
                pass
    var = {'forms': form}
    return render(request, 'add_funds.html', var)


def emp_funds_delete(request, id):
    funds = Funds.objects.get(pk=id)
    funds.delete()
    return redirect('/emp_fund_view')


def emp_allowance(request):
    allowance = Allowance.objects.all()
    return render(request, "allowance.html", {'allowance': allowance})


def emp_allowance_add(request):
    allowance = AllowanceForm()
    if request.method == 'POST':
        allowance = AllowanceForm(request.POST)
        if allowance.is_valid():
            try:
                allowance.save()
                return redirect('/emp_allowance')
            except:
                pass
    var = {'allowance': allowance}
    return render(request, 'add_allowance.html', var)


#Navigate from Admin home to Registered Suppliers List
@login_required(login_url='login')
def to_reg_suppliers(request):

    return render(request, 'AllRegisteredSuppliers.html')


#Navigate from Registered Suppliers List to Registration Form
@login_required(login_url='login')
def to_sup_registration(request):

    return render(request, 'SupRegistration.html')


#Navigate from Registered Suppliers List to View Supplier Profile
@login_required(login_url='login')
def to_sup_profile(request):

    return render(request, 'ViewSupplierProfile.html')


#Navigate from Supplier Profile to Edit Supplier
@login_required(login_url='login')
def to_edit_profile(request):

    return render(request, 'EditSupplier.html')


#Navigate from Registered Suppliers List to Stock Details
@login_required(login_url='login')
def to_stock_details(request):

    return render(request, 'StockDetails.html')


#Navigate from Stock Details to Add Leaf Stock
@login_required(login_url='login')
def to_leaf_stock(request):

    return render(request, 'LeafStock.html')


#Navigate from Stock Details to View Stock Details
@login_required(login_url='login')
def to_view_stock_details(request):
    # var = LeafStock.objects.select_related('supplier_id').get(pk=1)
    return render(request, 'ViewLeafStock.html')


#Navigate from Registered Suppliers List to Payments
@login_required(login_url='login')
def to_payments(request):

    return render(request, 'SupPayments.html')

