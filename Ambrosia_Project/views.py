from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ambrosia_Project.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Ambrosia_Project.models import *
from Ambrosia_Project.forms import *
from django.http import HttpResponse
from django.views.generic import View

from Ambrosia_Project.utils import render_to_pdf


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
    form = AddInventoryForm()
    if request.method == 'POST':
        form = AddInventoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Inventory details updated successfully')
                return redirect('NavigateToPreInv')
            except:
                pass

        else:
            messages.error(request, "Invalid Details")


    var = {'form': form}
    return render(request, 'add_inventory.html', var)


@login_required(login_url='login')
def NavigateToPrevInv(request):
    leaf = LeafInventory.objects.all()
    return render(request, 'View_pre_inv.html', {'leaf': leaf})

@login_required(login_url='login')
def NavigateToInvReport(request):
    leaf = LeafInventory.objects.all()
    return render(request,'inventoryPDF.html',{'leaf':leaf})

@login_required(login_url='login')
def NavigateToUpdateInv(request):

    if request.method == 'POST':
        inv_ID = request.POST.get('lid')

        if inv_ID is not None:
            try:
                leaf = LeafInventory.objects.get(id=inv_ID)
                form = AddInventoryForm(instance=leaf)
                return render(request, 'update_inventory.html', {'form': form, 'lid':inv_ID })

            except Exception as e:
                print(e)

        else:
            #id is null
            pass
    else:
        #method is not post
        pass


    return render(request, 'View_pre_inv.html' )



@login_required(login_url='login')
def DeleteInv(request, id):
    leaf = LeafInventory.objects.get(pk=id)
    leaf.delete()
    return redirect('NavigateToPreInv')


@login_required(login_url='login')
def NavigateToProduction(request):

    form = AddSubProductForm()
    mFrom = AddMainProductForm()
    genID = 0

    #generate sub id
    mainProduct = Final_product_Main.objects.last()

    if mainProduct is not None:
        genID = mainProduct.subID + 1
    else:
        genID = 1

    if request.method == 'POST':

        form = AddSubProductForm(request.POST)

        if form.is_valid():

            try:
                productObj = form.save(commit=False)
                productObj.subID = genID
                productObj.save()

                messages.success(request, 'Successfully Added')
                return redirect('final_production_home')

            except Exception as e:
                print(e)
                messages.error(request, 'Exception')

        else:
            print(form.errors)
            messages.error(request, 'Invalid Details')

    #get subfinal production details
    subFinal = Final_product_sub.objects.filter(subID=genID)

    var = {'form': form,
           'mainForm': mFrom,
           'subID': genID,
           'finalSubProduct': subFinal
           }

    return render(request, 'Add_daily_product.html', var)


@login_required(login_url='login')
def addMainFinalProduction(request):

#calculate total weight
    total = 0
    allProduct = Final_product_sub.objects.all()

    for product in allProduct:
        total = total + product.gradeWeight


    if request.method == 'POST':
        sid = request.POST.get('sID')

        form = AddMainProductForm(request.POST)

        if form.is_valid():
            mainObj = form.save(commit=False)
            mainObj.subID = sid
            mainObj.totalWeight = total
            mainObj.save()

        else:
            messages.error(request, "invalid")


    return  redirect('final_production_home')



@login_required(login_url='login')
def NavigateToCustomDailyProd(request):
    prod = Final_product_Main.objects.all()
    return render(request, 'View_Daily_production.html',{'prod':prod})


@login_required(login_url='login')
def NavigateToCurrentProduct(request):
    return render(request, 'Current_product.html')


@login_required(login_url='login')
def NavigateToViewProduct(request):

    if request.method == 'POST':
        sid = request.POST.get('id')

        product = Final_product_sub.objects.filter(subID=sid)
        mainProd = Final_product_Main.objects.get(subID=sid)
        date = mainProd.date

    return render(request, 'sub_final_product_view.html', { 'products': product, 'date': date })


@login_required(login_url='login')
def DeleteLeaf(request):

    leafid = request.POST.get('leafid')

    if request.method == 'POST' and leafid is not None:
        leaf = LeafInventory.objects.get(id=leafid)
        leaf.delete()

    return redirect('NavigateToPreInv')


@login_required(login_url='login')
def LeafInvAdd(request):

    inDate = request.POST.get('inDate')

    if request.method == 'POST' and inDate is not None:
        form = LeafInventory.get(id=inDate)
        form.save()
    return render(request, 'View_pre_inv.html')


@login_required(login_url='login')
def updateLeaf(request):

    if request.method == 'POST':
        leafID = request.POST.get('LID')

        if leafID is not None:

            try:
                leaf = LeafInventory.objects.get(pk=leafID)
                form = AddInventoryForm(request.POST, instance=leaf)

                if form.is_valid():
                    form.save()

                    return redirect('NavigateToPreInv')

                else:
                    #validate
                    pass

            except Exception as e:
                print(e)

        else:
            #id is null
            pass

    return redirect('NavigateToPreInv')


def NavigateToDelSubPr(request):

    spr = request.POST.get('spr')

    if request.method == 'POST' and spr is not None:
        subpro = Final_product_sub.objects.get(id=spr)
        subpro.delete()


    return redirect('final_production_home')


def NavigateToTeaGrades(request):
    form = AddTeaGradeform()
    if request.method == 'POST':
        form = AddTeaGradeform(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Tea grade updated successfully')
                return redirect('NavigateToTeaGrades')
            except:
                pass
    grade = TeaGrades.objects.all()

    var = {'form': form,
           'grade': grade}



    return render(request, 'TeaGrades.html',var)


def DeleteGrade(request):
    grade = request.POST.get('grade')

    if request.method == 'POST' and grade is not None:
        gradeT = TeaGrades.objects.get(id=grade)
        gradeT.delete()

    return redirect('NavigateToTeaGrades')

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(),
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
