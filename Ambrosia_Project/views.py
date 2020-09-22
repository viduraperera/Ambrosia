from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Ambrosia_Project.forms import *

from Ambrosia_Project.forms import CreateUserForm
from django.contrib.auth.models import User
from Ambrosia_Project.models import *

from Ambrosia_Project.view_mappings.finalProductionAuctionViews import *

# Create your views here.

#Home Navigations------------------------------------------------------------------------------------------

@login_required(login_url='login')
def home(request):

    return render(request, 'home.html')

@login_required(login_url='login')
def factoryhome(request):
    return render(request, 'factoryhome.html')


@login_required(login_url='login')
def teashopHomepage (request):

    return render(request, 'teashophome.html')

#User Profile-----------------------------------------------------------------------------------------


@login_required(login_url='login')
def logout_user(request):

    logout(request)
    return redirect('login')


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
    return render(request, 'registration.html', context)


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
def view_AllUsers(request):

    array = User.objects.all()
    return render(request, 'ViewAllUsers.html', {'Users': array})


@login_required(login_url='login')
def ShowUser(request):

    uname = request.POST.get("uname")

    user = User.objects.get(username=uname);
    form = UserCreationForm(instance=user)

    if user is not None:
        return render(request, 'updateUser.html', {'UserDetails': user, 'form': form })

    else:
        #user not found
        pass

    return render(request, 'ViewAllUsers.html')


@login_required(login_url='login')
def UpdateUser(request):

    if request.method == 'POST':
        uname = request.POST.get('un')

        if uname is not None:
            user = User.objects.get(username=uname)
            userFrom = CreateUserForm(request.POST, instance=user)

            if userFrom.is_valid():
                objUser = userFrom.save(commit=False)
                objUser.username = uname
                objUser.save()
                messages.success(request, "User Details Updated Successfully")
                return redirect('view_all_users')

            else:
                messages.error(request, "Invalid Details.")
                return redirect('update_user')

        else:
            messages.error(request, "Can't Update Details.")
            return redirect('view_all_users')

    else:
        messages.error(request, "Can't Update Details.")
        return redirect('view_all_users')

    # messages.error(request, "Error.Can't Update Details.")
    # return redirect('view_all_users')


@login_required(login_url='login')
def DeleteUser(request):

    if request.method == 'POST':
        uname = request.POST.get('uname')

        if uname is not None:
            user = User.objects.get(username=uname)
            user.delete()
            messages.success(request, "User Deleted Successfully")
            return redirect('view_all_users')

        else:
            #user not found
            pass

    else:
        messages.error(request, "Can't Delete User.")
        return redirect('view_all_users')

    # messages.error(request, "Error.Can't Delete User.")
    # return redirect('view_all_users')

#Employee Management-----------------------------------------------------------------------------------------


@login_required(login_url='login')
def EmployeeHome (request):

    return render(request, 'attendance_management.html')


@login_required(login_url='login')
def staff_management (request):

    return render(request, 'staff_management.html')


@login_required(login_url='login')
def factoryworkers_management(request):

    return render(request, 'factoryworkers_management.html')


@login_required(login_url='login')
def markAttendance(request):

    return render(request, 'mark_attendance.html')


@login_required(login_url='login')
def edit_employee(request):

    return render(request, 'edit_employee.html')


@login_required(login_url='login')
def view_employee(request):

    return render(request, 'view_employee.html')


@login_required(login_url='login')
def employee_registration(request):

    return render(request, 'employee_registration.html')


@login_required(login_url='login')
def inventoryhome (request):

    return render(request, 'inventoryhome.html')


@login_required(login_url='login')
def addteapackets (request):

    return render(request, 'addteapackets.html')


@login_required(login_url='login')
def preorderlevel (request):

    return render(request, 'preorderlevel.html')
    # messages.error(request, "Error.Can't Delete User.")
    # return redirect('view_all_users')


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
def SalesHomeIncome(request):

    return render(request, 'SalesHomeIncome.html')


@login_required(login_url='login')
def SalesHomeMonthlyIncome(request):

    return render(request, 'SalesHomeMonthlyIncome.html')


@login_required(login_url='login')
def SalesHomeAnnuallyIncome(request):

    return render(request, 'SalesHomeAnnuallyIncome.html')


@login_required(login_url='login')
def SalesCreateInvoice(request):

    return render(request, 'SalesCreateInvoice.html')


@login_required(login_url='login')
def SalesTransaction(request):

    return render(request, 'SalesTransaction.html')


@login_required(login_url='login')
def SalesViewBill(request):

    return render(request, 'SalesViewBill.html')


@login_required(login_url='login')
def SalesPriceTable(request):

    return render(request, 'SalesPriceTable.html')


@login_required(login_url='login')
def SalesPriceTableDUST1(request):

    return render(request, 'SalesPriceTableDUST1.html')


@login_required(login_url='login')
def SalesPriceTableDUST2(request):

    return render(request, 'SalesPriceTableDUST2.html')


@login_required(login_url='login')
def SalesPriceTableDUST3(request):

    return render(request, 'SalesPriceTableDUST3.html')


@login_required(login_url='login')
def SalesPriceTableFGS(request):

    return render(request, 'SalesPriceTableFGS.html')


@login_required(login_url='login')
def emp_funds_delete(request, id):
    funds = Funds.objects.get(pk=id)
    funds.delete()
    return redirect('emp_fund_view')


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


@login_required(login_url='login')
def inventoryreports (request):
    return render(request, 'inventoryreports.html')


@login_required(login_url='login')
def iweekly (request):
    return render(request, 'iweekly.html')


@login_required(login_url='login')
def inventorymonthlyreport (request):
    return render(request, 'inventorymonthlyreport.html')


@login_required(login_url='login')
def inventoryannualreport (request):
    return render(request, 'inventoryannualreport.html')


@login_required(login_url='login')
def editpackets (request):

    return render(request, 'editpackets.html')


#Leaf Inventory-------------------------------------------------------------------------------------------


@login_required(login_url='login')
def NavigateToInventory(request):
    return render(request, 'add_inventory.html')


@login_required(login_url='login')
def NavigateToPrevInv(request):
    return render(request, 'View_pre_inv.html')


@login_required(login_url='login')
def NavigateToUpdateInv(request):
    return render(request, 'update_inventory.html')


#Final production -------------------------------------------------------------------------------------------

#Daily Production------------------------------------------------------------------------------------------


@login_required(login_url='login')
def finalProductionHome(request):
    return render(request, 'finalproductionhome.html')


@login_required(login_url='login')
def NavigateToProduction(request):
    return render(request, 'Add_daily_product.html')


@login_required(login_url='login')
def NavigateToCustomDailyProd(request):
    return render(request, 'View_Daily_production.html')


def NavigateToTeaGrades(request):
    return render(request, 'TeaGrades.html')


@login_required(login_url='login')
def NavigateToCurrentProduct(request):
    return render(request, 'Current_product.html')


@login_required(login_url='login')
def NavigateToUpdateProduct(request):
    return render(request, 'Update_daily_product.html')
