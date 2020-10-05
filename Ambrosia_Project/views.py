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
            messages.success(request, 'User Account ' + user + ' Created Successfully.')
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
def teashopHomepage(request):
    return render(request, 'teashophome.html')


@login_required(login_url='login')
def EmployeeHome(request):
    return render(request, 'attendance_management.html')


@login_required(login_url='login')
def staff_management(request):
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


# @login_required(login_url='login')
# def AddUser(request):


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
        pword = request.POST.get('pwd')

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

    # messages.error(request, "Error.Can't Update Details.")
    # return redirect('view_all_users')


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


@login_required(login_url='login')
def inventoryhome(request):
    return render(request, 'inventoryhome.html')


@login_required(login_url='login')
def addteapackets(request):
    return render(request, 'addteapackets.html')


@login_required(login_url='login')
def preorderlevel(request):
    return render(request, 'preorderlevel.html')
    # messages.error(request, "Error.Can't Delete User.")
    # return redirect('view_all_users')

# ---------------------------start of funds of employee-----------------------------------


@login_required(login_url='login')
def emp_fund_view(request):
    funds = Funds.objects.all()
    return render(request, "funds_table.html", {'funds': funds})


@login_required(login_url='login')
def employee_salary_front(request):
    salary_month = EmployeeSalaryMonth.objects.all()
    return render(request, 'employee_salary.html', {'salary_month': salary_month})


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
def emp_salary_month_add(request):
    form = EmployeeSalaryMonthFrom(request.POST)
    if form.is_valid():
        try:
            form.save()
            return redirect('employee_salary_front')
        except:
            pass
    var = {'form': form}
    return render(request, 'employee_salary_month_add.html', var)


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


def ShopPriceTableBOPFUpdate(request):
    return render(request, 'ShopPriceTableBOPFUpdate.html')


def ShopPriceTableFGSUpdate(request):
    return render(request, 'ShopPriceTableFGSUpdate.html')


def ShopPriceTableDUST1Update(request):
    return render(request, 'ShopPriceTableDUST1Update.html')


def ShopPriceTableDUST2Update(request):
    return render(request, 'ShopPriceTableDUST2Update.html')


# Navigate from Admin home to Registered Suppliers List
@login_required(login_url='login')
def to_reg_suppliers(request):
    return render(request, 'AllRegisteredSuppliers.html')


# Navigate from Registered Suppliers List to Registration Form
@login_required(login_url='login')
def to_sup_registration(request):
    return render(request, 'SupRegistration.html')


# Navigate from Registered Suppliers List to View Supplier Profile
@login_required(login_url='login')
def to_sup_profile(request):
    return render(request, 'ViewSupplierProfile.html')


# Navigate from Supplier Profile to Edit Supplier
@login_required(login_url='login')
def to_edit_profile(request):
    return render(request, 'EditSupplier.html')


# Navigate from Registered Suppliers List to Stock Details
@login_required(login_url='login')
def to_stock_details(request):
    return render(request, 'StockDetails.html')


# Navigate from Stock Details to Add Leaf Stock
@login_required(login_url='login')
def to_leaf_stock(request):
    return render(request, 'LeafStock.html')


# Navigate from Stock Details to View Stock Details
@login_required(login_url='login')
def to_view_stock_details(request):
    # var = LeafStock.objects.select_related('supplier_id').get(pk=1)
    return render(request, 'ViewLeafStock.html')


# Navigate from Registered Suppliers List to Payments
@login_required(login_url='login')
def to_payments(request):
    return render(request, 'SupPayments.html')


@login_required(login_url='login')
def inventoryreports(request):
    return render(request, 'inventoryreports.html')


@login_required(login_url='login')
def iweekly(request):
    return render(request, 'iweekly.html')


@login_required(login_url='login')
def inventorymonthlyreport(request):
    return render(request, 'inventorymonthlyreport.html')


@login_required(login_url='login')
def inventoryannualreport(request):
    return render(request, 'inventoryannualreport.html')


@login_required(login_url='login')
def editpackets(request):
    return render(request, 'editpackets.html')
    messages.error(request, "Error.Can't Delete User.")
    return redirect('view_all_users')


@login_required(login_url='login')
def factoryhome(request):
    return render(request, 'factoryhome.html')


@login_required(login_url='login')
def finalProductionHome(request):
    return render(request, 'finalproductionhome.html')


@login_required(login_url='login')
def AuctionStockHome(request):
    return render(request, 'addAuction_stock.html')


@login_required(login_url='login')
def ShowAuctionStock(request):
    return render(request, 'catelogDetails.html')


@login_required(login_url='login')
def StockSalesHome(request):
    return render(request, 'auctionStock_current.html')


@login_required(login_url='login')
def UpdateAuctionStock(request):
    return render(request, 'updateCatelog.html')


@login_required(login_url='login')
def ShowBrokerDetails(request):
    return render(request, 'AllBrokers.html')


@login_required(login_url='login')
def ShowBuyerDetails(request):
    return render(request, 'AllBuyer.html')


@login_required(login_url='login')
def AddNewBroker(request):
    return render(request, 'addBroker.html')


@login_required(login_url='login')
def AddNewBuyer(request):
    return render(request, 'addBuyer.html')


@login_required(login_url='login')
def UpdateBroker(request):
    return render(request, 'updateBroker.html')


@login_required(login_url='login')
def UpdateBuyer(request):
    return render(request, 'updateBuyer.html')


@login_required(login_url='login')
def ProductionAnalysisHome(request):
    return render(request, 'finalProductAnalysis.html')


def NotSoldStock(request):
    return render(request, 'auction_notSold.html')


def SoldStock(request):
    return render(request, 'auction_soldStock.html')


@login_required(login_url='login')
def NavigateToInventory(request):
    return render(request, 'add_inventory.html')


@login_required(login_url='login')
def NavigateToPrevInv(request):
    return render(request, 'View_pre_inv.html')


@login_required(login_url='login')
def NavigateToUpdateInv(request):
    return render(request, 'update_inventory.html')


@login_required(login_url='login')
def NavigateToProduction(request):
    return render(request, 'Add_daily_product.html')


@login_required(login_url='login')
def NavigateToCustomDailyProd(request):
    return render(request, 'View_Daily_production.html')


@login_required(login_url='login')
def NavigateToCurrentProduct(request):
    return render(request, 'Current_product.html')


@login_required(login_url='login')
def NavigateToUpdateProduct(request):
    return render(request, 'Update_daily_product.html')


