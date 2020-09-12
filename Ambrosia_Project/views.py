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
def home(request):

    return render(request, 'home.html')


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

    if user is not None:
        return render(request, 'updateUser.html', {'UserDetails': user})

    else:
        #user not found
        pass

    return render(request, 'ViewAllUsers.html')


@login_required(login_url='login')
def UpdateUser(request):

    if request.method == 'POST':
        uname = request.POST.get('un')
        pword =request.POST.get('pwd')

        if uname is not None and pword is not None:
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


@login_required(login_url='login')
def factoryHomepage(request):

    return render(request, 'factoryhome.html')


@login_required(login_url='login')
def teashopHomepage (request):

    return render(request, 'teashophome.html')


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
    messages.error(request, "Error.Can't Delete User.")
    return redirect('view_all_users')


@login_required(login_url='login')
def factoryhome(request):
    return render(request, 'factoryhome.html')


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


@login_required(login_url='login')
def finalProductionHome(request):
    return render(request, 'finalproductionhome.html')

#auction stock--------------------------------------------------------------------------------------------

@login_required(login_url='login')
def AddAuctionStock(request):

    form_auction = AddAuctionStockForm()

    return render(request, 'addAuction_stock.html', {'form': form_auction} )


@login_required(login_url='login')
def ShowAuctionStock(request):
    return render(request, 'catelogDetails.html')


@login_required(login_url='login')
def StockSalesHome(request):
    return render(request, 'auctionStock_current.html')


@login_required(login_url='login')
def UpdateAuctionStock(request):
    return render(request, 'updateCatelog.html')

#Broker-----------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def ShowBrokerDetails(request):

    try:
        arr = Broker.objects.all()

    except:
        pass

    return render(request, 'AllBrokers.html', {'Brokers': arr})


@login_required(login_url='login')
def AddNewBroker(request):

    form = AddBrokerForm()

    if request.method == 'POST':
        form = AddBrokerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('all_brokers')
            except:
                pass
        else:
            #form is not valid
            pass

    else:
        #form method is not post
        pass

    var = {'form': form}
    return render(request, 'addBroker.html', var)


@login_required(login_url='login')
def ShowBroker(request):

    if request.method == 'POST':
        brID = request.POST.get('bID')

        if brID is not None:

            try:
                broker = Broker.objects.get(pk=brID)

                if broker is not None:
                    return render(request, 'updateBroker.html', {'Broker': broker})

                else:
                    #broker not found
                    pass

            except:
                pass

        else:
            #broker id is empty
            pass

    else:
        #form method is not POST
        pass

    return render(request, 'AllBrokers.html')


@login_required(login_url='login')
def UpdateBroker(request):

    if request.method == 'POST':
        brID = request.POST.get('bId')

        if brID is not None:
            brName = request.POST.get('bName')
            brPhone = request.POST.get('bPhone')
            brAddress = request.POST.get('bAddress')

            try:
                broker = Broker.objects.get(pk=brID)

                if broker is not None:
                    broker.name = brName
                    broker.phone = brPhone
                    broker.address = brAddress
                    broker.save()
                    return redirect('all_brokers')

                else:
                    #broker not found in db
                    pass

            except:
                pass

        else:
            #BRokerId is NUll
            pass

    else:
        #form method is not POST
        pass

    return render(request, 'updateBroker.html')


@login_required(login_url='login')
def deleteBroker(request):

    if request.method == 'POST':
        brokerid = request.POST.get('brokerid')

        if brokerid is not None:

            try:
                broker = Broker.objects.get(pk=brokerid)

                if broker is not None:
                    broker.delete()

                else:
                    # broker not found
                    pass

            except:
                pass

        else:
            #broker id is null
            pass

    else:
        #form method is not POST
        pass

    return redirect('all_brokers')


#Buyer---------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def AddNewBuyer(request):

    form = AddBuyerForm()

    if request.method == 'POST':
        form = AddBuyerForm(request.POST)

        if form.is_valid():
            try:
                #vatNo = form.cleaned_data.get('vat_regno')
                #print("VAT REG NO:",vatNo)
                form.save()
                messages.success(request, 'Sucessfully Added Buyer Details')
                return redirect('all_buyers')

            except Exception as e:
                # pass
                print(e)
                messages.success(request, 'Exception:'+e)
                return redirect('add_buyer')
        else:
            #form method is not valid
            print(form.errors)
            messages.success(request, 'Invalid Details')
            pass

    #poss form to add buyer
    var = {'form': form}
    return render(request, 'addBuyer.html', var)


@login_required(login_url='login')
def ShowBuyerDetails(request):

    try:
        buyersArr = Buyer.objects.all()

    except Exception as e:
        print(e)
        messages.success(request, 'Exception: '+e)

    return render(request, 'AllBuyer.html', {'Buyers': buyersArr})


@login_required(login_url='login')
def ShowBuyer(request):

    if request.method == 'POST':
        buyerID = request.POST.get('buyerID')

        if buyerID is not None:
            try:
                buyer = Buyer.objects.get(pk=buyerID)
                buyerform = AddBuyerForm(instance=buyer)
                return render(request, 'updateBuyer.html', {'BuyerForm': buyerform, 'BId': buyerID})

            except Exception as e:
                print(e)
                messages.success(request, 'Exception :'+e)

    return render(request, 'AllBuyer.html')


@login_required(login_url='login')
def UpdateBuyer(request):

    if request.method == "POST":

        try:
            buyerform = AddBuyerForm(request.POST)
            buyerid = request.POST.get('bID')

            if buyerform.is_valid():

                    buyer = Buyer.objects.get(pk=buyerid)

                    if buyer is not None:
                        buyer_form = AddBuyerForm(request.POST, instance=buyer)
                        buyer_form.save()
                        messages.success(request, 'Sucessfully updated Buyer Details')
                        return redirect('all_buyers')

                    else:
                        #if buyer not found in db
                        messages.success(request, 'Buyer details not found in database')

            #form is not valid
            else:
                print(buyerform.errors)
                messages.success(request, 'Invalid Details')
                return render(request, 'updateBuyer.html', {'BuyerForm': buyerform, 'BId': buyerid})

        except Exception as e:
            print(e)
            messages.success(request, 'Exception :' + e)

    else:
        #form method is not
        messages.success(request, 'Form method is invalid')
        return redirect('all_buyers')

    return redirect('all_buyers')


@login_required(login_url='login')
def DeleteBuyer(request):

    if request.method == "POST":
        buyerid = request.POST.get('buyerID')

        if buyerid is not None:

            try:
                buyer = Buyer.objects.get(pk=buyerid)

                if buyer is not None:
                    buyer.delete()
                    messages.success(request, 'Buyer Details Deleted Successfully.')

                else:
                    #buyer is not found in db
                    messages.success(request, 'Buyer Not Found in Database')

            except Exception as e:
                print(e)
                messages.success(request, 'Exception :'+e)

        else:
            #buyer id is null
            messages.success(request, 'Passed Buyer id is Null.')

    else:
        #form method is not POST
        messages.success(request, 'Form method is invalid')

    return redirect('all_buyers')
