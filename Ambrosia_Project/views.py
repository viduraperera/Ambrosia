from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ambrosia_Project.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Ambrosia_Project.models import *
from Ambrosia_Project.forms import *
from Ambrosia_Project.commonUtills import *
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


#Auction stock--------------------------------------------------------------------------------------------


@login_required(login_url='login')
def addAuctionSubStock(request):

    subForm = AddSubAuctionStockForm()
    mainStForm = AddMainAuctionStockForm()
    sid = generateSubStockID()

    if request.method == 'POST':
        Sfrom = AddSubAuctionStockForm(request.POST)

        try:
            if Sfrom.is_valid():
                formobj = Sfrom.save(commit=False)
                formobj.SubID = sid
                formobj.status = 'Pending'
                formobj.save()
                messages.success(request, 'Record Added Sucessfully')
                return redirect('prepare_auction_stock')

            else:
                messages.error(request, 'Invalid Data provided')
                return redirect('prepare_auction_stock')

        except Exception as e:
            print(e)
            messages.error(request, 'Exception')
            return redirect('prepare_auction_stock')

    #All calculations
    subStock = calculaionsAuctionSubStock(sid)

    var = { 'form': subForm,
            'mForm': mainStForm,
            'SubStock':subStock,
            'sid': sid,
            }

    return render(request, 'addAuction_stock.html', var)


@login_required(login_url='login')
def deleteAuctionSubStock(request):

    if request.method == 'POST':
        sid = request.POST.get('stID')

        if sid is not None:
            stock = Auction_SubStock.objects.get(pk=sid)

            if stock is not None:
                stock.delete()
                messages.success(request, 'Successfully Deleted')
                # return redirect('prepare_auction_stock')
                return redirect(request.META['HTTP_REFERER'])

            else:
                messages.error(request, 'Stock not found in database')

        else:
            messages.error('Stock id is null')

    else:
        return redirect('prepare_auction_stock')


@login_required(login_url='login')
def addMainAuctionStock(request):

    if request.method == 'POST':
        subID = request.POST.get('sid')
        netW = request.POST.get('tnet')
        grossW = request.POST.get('tgr')
        pkts = request.POST.get('tpk')

        #get form
        mainForm = AddMainAuctionStockForm(request.POST)

        try:
            if mainForm.is_valid():
                dbObject = mainForm.save(commit=False)
                dbObject.SubID = subID
                dbObject.total_netWeight = netW
                dbObject.total_grossWeight = grossW
                dbObject.total_packets = pkts
                dbObject.save()
                messages.success(request, 'Sucessfully Created Catelog')
                return redirect('all_catelog')

            #for mdetails invalid
            else:
                messages.error(request, 'Invalid Details')
                return redirect('prepare_auction_stock')

        except Exception as e:
            print(e)
            messages.error(request, 'Exception')
            return redirect('prepare_auction_stock')


    return redirect('prepare_auction_stock')


@login_required(login_url='login')
def showAuctionMainStocks(request):

    try:
        allCatelogs = Auction_MainStock.objects.all()
        return render(request, 'catelogDetails.html', {'MainStocks':allCatelogs})

    except Exception as e:
        print(e)

    return redirect('prepare_auction_stock')


@login_required(login_url='login')
def showMainAuctionStock(request):

    if request.method == 'POST':

        sid = request.POST.get('sid')

        try:
            stocks = calculaionsAuctionSubStock(sid)

            if stocks is not None:
                return render(request, 'viewCatelog.html', {'subStocks': stocks})

            else:
                return redirect('all_catelog')

        except Exception as e:
            print(e)

    return redirect('all_catelog')


@login_required(login_url='login')
def notSoldStock(request):
    return render(request, 'auction_notSold.html')


@login_required(login_url='login')
def soldStock(request):

    return render(request, 'auction_soldStock.html')


@login_required(login_url='login')
def stockSalesHome(request):
    return render(request, 'auctionStock_current.html')


@login_required(login_url='login')
def updateAuctionStock(request):
    return render(request, 'updateCatelog.html')


#Production Analysis--------------------------------------------------------------------------------------------


@login_required(login_url='login')
def productionAnalysisHome(request):
    return render(request, 'finalProductAnalysis.html')


#Broker-----------------------------------------------------------------------------------------------------


@login_required(login_url='login')
def showBrokerDetails(request):

    try:
        arr = Broker.objects.all()
        return render(request, 'AllBrokers.html', {'Brokers': arr})

    except Exception as e:
        print(e)
        messages.error(request, "Exception")
        return render(request, 'AllBrokers.html')


@login_required(login_url='login')
def addNewBroker(request):

    form = AddBrokerForm()

    if request.method == 'POST':
        form = AddBrokerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'SUccessfully Added Broker Details')
                return redirect('all_brokers')

            except Exception as e:
                print(e)
                messages.error(request, 'Exception')

        else:
            messages.error(request, 'Invalid Details')

    else:
        #form method is not POST
       pass

    var = {'form': form}
    return render(request, 'addBroker.html', var)


@login_required(login_url='login')
def showBroker(request):

    if request.method == 'POST':
        brID = request.POST.get('bID')

        if brID is not None:

            try:
                broker = Broker.objects.get(pk=brID)
                brokerForm = AddBrokerForm(instance=broker)

                if broker is not None:
                    return render(request, 'updateBroker.html', {'Broker': brokerForm, 'BrokerID' : brID})

                else:
                    messages.error(request, 'Broker not found in Database')
                    return redirect('all_brokers')

            except Exception as e:
                print(e)
                messages.error(request, 'Exception')

        else:
            messages.error(request, 'Broker id is empty')

    else:
        messages.error(request, 'Form method is invalid')


    return redirect('all_brokers')


@login_required(login_url='login')
def updateBroker(request):

    if request.method == 'POST':
        brID = request.POST.get('bId')

        if brID is not None:

            try:
                broker = Broker.objects.get(pk=brID)
                bFrom = AddBrokerForm(request.POST, instance=broker)

                if bFrom.is_valid():
                    bFrom.save()
                    messages.success(request, 'Successfully Updated Broker Details')
                    return redirect('all_brokers')

                else:
                    #Not Valid
                    messages.success(request, 'Invalid Details Provided.')
                    return render(request, 'updateBroker.html', {'Broker': bFrom, 'BrokerID': brID})

            except Exception as e:
                print(e)
                messages.error(request, 'Exception Occured')
                return redirect('all_brokers')

        else:
            #BRokerId is NUll
            messages.error(request, 'Broker id is Null')
            return redirect('all_brokers')

    return redirect('all_brokers')


@login_required(login_url='login')
def deleteBroker(request):

    if request.method == 'POST':
        brokerid = request.POST.get('brokerid')

        if brokerid is not None:

            try:
                broker = Broker.objects.get(pk=brokerid)

                if broker is not None:
                    messages.success(request, 'Sucessfully Deleted Details')
                    broker.delete()

                else:
                    messages.error(request, 'Broker not found in database')

            except Exception as e:
                print(e)
                messages.error(request, 'Exception')

        else:
            messages.error(request, 'Broker id is null')

    else:
        messages.error(request, 'Form method is invalid')

    return redirect('all_brokers')


#Buyer---------------------------------------------------------------------------------------------------------


@login_required(login_url='login')
def addNewBuyer(request):

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
                messages.error(request, 'Exception')
                return redirect('add_buyer')
        else:
            #form method is not valid
            print(form.errors)
            messages.error(request, 'Invalid Details')
            pass

    #poss form to add buyer
    var = {'form': form}
    return render(request, 'addBuyer.html', var)


@login_required(login_url='login')
def showBuyerDetails(request):

    try:
        buyersArr = Buyer.objects.all()
        return render(request, 'AllBuyer.html', {'Buyers': buyersArr})

    except Exception as e:
        print(e)
        messages.error(request, 'Exception')
        return render(request, 'AllBuyer.html')


@login_required(login_url='login')
def showBuyer(request):

    if request.method == 'POST':
        buyerID = request.POST.get('buyerID')

        if buyerID is not None:
            try:
                buyer = Buyer.objects.get(pk=buyerID)
                buyerform = AddBuyerForm(instance=buyer)
                return render(request, 'updateBuyer.html', {'BuyerForm': buyerform, 'BId': buyerID})

            except Exception as e:
                print(e)
                messages.error(request, 'Exception')

    return render(request, 'AllBuyer.html')


@login_required(login_url='login')
def updateBuyer(request):

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
                        messages.error(request, 'Buyer details not found in database')

            #form is not valid
            else:
                print(buyerform.errors)
                messages.success(request, 'Invalid Details')
                return render(request, 'updateBuyer.html', {'BuyerForm': buyerform, 'BId': buyerid})

        except Exception as e:
            print(e)
            messages.error(request, 'Exception')

    else:
        #form method is not
        messages.error(request, 'Form method is invalid')
        return redirect('all_buyers')

    return redirect('all_buyers')


@login_required(login_url='login')
def deleteBuyer(request):

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
                messages.error(request, 'Exception')

        else:
            #buyer id is null
            messages.error(request, 'Passed Buyer id is Null.')

    else:
        #form method is not POST
        messages.error(request, 'Form method is invalid')

    return redirect('all_buyers')
