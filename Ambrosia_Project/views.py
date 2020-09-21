from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import View

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


#Auction stock--------------------------------------------------------------------------------------------


@login_required(login_url='login')
def addAuctionSubStock(request):

    subForm = AddSubAuctionStockForm()
    mainStForm = AddMainAuctionStockForm()
    sid = generateSubStockID()

    if request.method == 'POST':
        subForm = AddSubAuctionStockForm(request.POST)

        try:
            if subForm.is_valid():
                formobj = subForm.save(commit=False)
                formobj.SubID = sid
                formobj.status = 'Pending'
                formobj.save()
                messages.success(request, 'Record Added Sucessfully')
                return redirect('prepare_auction_stock')

            else:
                messages.error(request, 'Invalid Data provided')

        except Exception as e:
            print(e)
            messages.error(request, 'Exception')

    #All calculations
    subStock = calculaionsAuctionSubStock(sid)

    # get not sold stock relevent forms-----------------------------------------------
    prevSubStock = Auction_SubStock.objects.filter(status='Not Sold', active=1)
    notSoldStocks = Auction_NotSoldStocks.objects.filter(active=1)
    nAddFrom = AddSubAuctionStockForm()

    var = { 'form': subForm,
            'mForm': mainStForm,
            'SubStock':subStock,
            'sid': sid,
            'prevSubStock':prevSubStock,
            'notSoldStocks': notSoldStocks,
            'nAddForm': nAddFrom,
            }

    return render(request, 'addAuction_stock.html', var)


@login_required(login_url='login')
def deleteAuctionSubStock(request):

    if request.method == 'POST':
        mid = request.POST.get('stID')
        sid = request.POST.get('subID')

        try:
            if mid is not None:
                stock = Auction_SubStock.objects.get(pk=mid)
                mainStock = Auction_MainStock.objects.filter(SubID=sid)
                chk = Auction_MainStock.objects.filter(SubID=sid).exists()

                if stock is not None:
                    stock.delete()

                    if chk:
                        # All calculations
                        mStock = Auction_MainStock.objects.get(SubID=sid)
                        subSt = calculaionsAuctionSubStock(sid)
                        mStock.total_netWeight = subSt['tne']
                        mStock.total_grossWeight = subSt['tgr']
                        mStock.total_packets = subSt['tpk']
                        mStock.save()
                        messages.success(request, 'Successfully Deleted')
                        return redirect('view_mainStock')

                    else:
                        messages.success(request, 'Successfully Deleted')
                        return redirect('prepare_auction_stock')

                else:
                    messages.error(request, 'Sub Stock not found in database')

            else:
                messages.error(request,'Stock id is null')


        except Exception as e:
            print(e)
            messages.error(request, 'Exception ')

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
            sForm = AddSubAuctionStockForm()

            var =  {
                'subStocks': stocks,
                'form':sForm,
                'sid':sid
            }

            if stocks is not None:
                return render(request, 'viewCatelog.html',var)

            else:
                return redirect('all_catelog')

        except Exception as e:
            print(e)

    return redirect('all_catelog')


@login_required(login_url='login')
def afterAddAuctionSubStock(request):

    if request.method == 'POST':
        sID = request.POST.get('sid')
        Sfrom = AddSubAuctionStockForm(request.POST)

        try:
            if Sfrom.is_valid():
                #add sub stock
                formobj = Sfrom.save(commit=False)
                formobj.SubID = sID
                formobj.status = 'Pending'
                formobj.save()

                #update main stock All calculations
                subStockcal = calculaionsAuctionSubStock(sID)

                mainStock = Auction_MainStock.objects.get(SubID=sID)
                mainStock.total_netWeight = subStockcal['tne']
                mainStock.total_grossWeight = subStockcal['tgr']
                mainStock.total_packets = subStockcal['tpk']
                mainStock.save()

                messages.success(request, 'Record Added Sucessfully')
                return redirect('view_mainStock')

            else:
                messages.error(request, 'Invalid Data provided')
                return redirect('view_mainStock')

        except Exception as e:
            print(e)
            messages.error(request, 'Exception')
            return redirect('view_mainStock')


    return render(request, 'catelogDetails.html')


@login_required(login_url='login')
def viewAuctionSubStock(request):

    if request.method == 'POST':
        mID = request.POST.get('mid')

        if mID is not None:
            try:
                stock = Auction_SubStock.objects.get(pk=mID)
                form = AddSubAuctionStockForm(instance=stock)

                var = {
                    'form': form,
                    'stock':stock,
                }
                return render(request, 'viewAuctionSubStock.html', var)

            except Exception as e:
                print(e)
                messages.error(request, 'Exception')

    return redirect('all_catelog')


@login_required(login_url='login')
def updateAuctionSubStock(request):

    if request.method == 'POST':
        mainID = request.POST.get('mID')

        try:

            stock = Auction_SubStock.objects.get(pk=mainID)
            sid =stock.SubID
            form = AddSubAuctionStockForm(request.POST, instance=stock)

            if form.is_valid():
                subObject = form.save(commit=False)
                subObject.SubID = sid
                subObject.status = 'Pending'
                subObject.save()
                messages.success(request, 'Successfully Updated')
                return redirect('all_catelog')

            else:
                messages.error(request, 'Invalid Details')

        except Exception as e:
            messages.error(request, 'Exception')

    return redirect('all_catelog')


@login_required(login_url='login')
def addNotSoldToCurrentCatelog(request):

    if request.method == 'POST':
        newID = request.POST.get('newSID')
        prMainID = request.POST.get('prvMID')

        if newID is not None and prMainID is not None:
            newStockForm = AddSubAuctionStockForm(request.POST)

            #get previous stock details
            prvStock = Auction_SubStock.objects.get(pk=prMainID)

            try:

                if newStockForm.is_valid():
                    #add(prepare) new stock
                    newStock = newStockForm.save(commit=False)
                    newStock.SubID = newID
                    newStock.grade = prvStock.grade
                    newStock.packetType = prvStock.packetType
                    newStock.status = 'Pending'
                    newStock.save()

                    #delete(inactive) previous sub stock
                    prvStock.active = 0
                    prvStock.save()

                    #delete(inactive) not sold stock
                    prvNotSoldStock = Auction_NotSoldStocks.objects.get(MainID=prMainID)
                    prvNotSoldStock.active = 0
                    prvNotSoldStock.save()

                    #get new main id
                    newAddStock = Auction_SubStock.objects.last()
                    newMainID = str(newAddStock.id)

                    #addto Auction_RePreparedNotSoldStocksDetails details table
                    stDetail = Auction_RePreparedNotSoldStocksDetails()
                    stDetail.NewSubStockMainID = newMainID
                    stDetail.PreviousSubStockMainID = prMainID
                    stDetail.NotSoldStockID = prvNotSoldStock.id
                    stDetail.save()

                    #update log
                    notSoldlog = Auction_NotSoldStocksLog()
                    notSoldlog.Description = '<ReAddStock>: Add Not Sold Stock to new Catelog and Delete(inactive) Not sold table record. | ' \
                                             '<Previous Sub Stock Main ID >: '+prMainID+' | ' \
                                             '<New Sub Stock MainID>:'+newMainID+'  |<New Sub Stock SubID>: '+newID+''

                    notSoldlog.save()
                    messages.success(request, 'Sucessfully added to new Stock')
                    return redirect('prepare_auction_stock')

                else:
                    messages.error(request, 'invalid details')

            except Exception as e:
                print(e)
                messages.error(request, 'Exception')

        else:
            messages.error(request,'Id is null')


    return redirect('prepare_auction_stock')


#Auction Sales-------------------------------------------------------------------------------------------


@login_required(login_url='login')
def stockSalesHome(request):

    try:
        curStocks = Auction_SubStock.objects.filter(status='Pending', active=1)
        return render(request, 'auctionStock_current.html', {'stock': curStocks})

    except Exception as e:
        messages.error(request, 'Exception')
        print(e)

    return redirect('stock_sales')


@login_required(login_url='login')
def viewAddSoldStock(request):

    if request.method == 'POST':
        mid = request.POST.get('mID')

        if mid is not None:
            mStock = Auction_SubStock.objects.get(pk=mid)
            mForm = AddAuctionSoldStockForm()

            var = {
                'stk': mStock,
                'form': mForm
            }

            return render(request, 'AddSoldStock.html', var)


@login_required(login_url='login')
def AddSoldStock(request):

    if request.method == 'POST':
        mainid = request.POST.get('mID')
        subid = request.POST.get('sID')

        try:
            if mainid is not None and subid is not None:
                soldForm = AddAuctionSoldStockForm(request.POST)

                if soldForm.is_valid():
                    # calculate total price
                    current = Auction_SubStock.objects.get(pk=mainid)
                    netW = current.net_weight
                    total = soldForm.cleaned_data['price'] * netW

                    #save sold stock
                    sold = soldForm.save(commit=False)
                    sold.total_price = total
                    sold.MainID = mainid
                    sold.SubID = subid
                    sold.save()

                    #update current stock
                    current.status = 'Sold'
                    current.save()

                    messages.success(request, 'Successfully Added to Sold Stocks')
                    return redirect('stock_sold')

                else:
                    messages.error(request, 'Invalid Details')
                    mStock = Auction_SubStock.objects.get(pk=mainid)
                    mForm = AddAuctionSoldStockForm()

                    var = {
                        'stk': mStock,
                        'form': mForm
                    }
                    return render(request, 'AddSoldStock.html', var)

            else:
                messages.error(request, 'Error Main/Sub ID is null')
                return redirect('stock_sales')

        except Exception as e:
            print(e)
            messages.error(request, 'Exception: ')
            return redirect('stock_sales')

    return redirect('stock_sales')


@login_required(login_url='login')
def soldStock(request):

    try:
        sold = Auction_SoldStocks.objects.filter(active=1)
        substocks = Auction_SubStock.objects.filter(status='Sold', active=1)
        return render(request, 'auction_soldStock.html', {'soldStocks': sold , 'subStocks':substocks })

    except Exception as e:
        print(e)
        messages.error(request, 'Exception')
        return render(request, 'auction_soldStock.html')


@login_required(login_url='login')
def showSoldAuctionSubStock(request):

    if request.method == 'POST':
        mid = request.POST.get('sID')
        soldId = request.POST.get('soldID')

        if mid is not None and soldId is not None:
            soldStock = Auction_SoldStocks.objects.get(pk=soldId)
            form = AddAuctionSoldStockForm(instance=soldStock)
            subStock = Auction_SubStock.objects.get(pk=mid)

            totPrice = soldStock.total_price

            var = {
                'stk':subStock,
                'form': form,
                'soldStockId': soldId,
                'totalPrice':totPrice
            }
            return render(request, 'updateSoldStock.html', var)

        else:
            messages.error(request, 'Error mid/soldId is null')
            return redirect('stock_sold')

    return redirect('stock_sold')


@login_required(login_url='login')
def updateSoldAuctionSubStock(request):

    if request.method == 'POST':
        soldStId = request.POST.get('soldStockID')
        mainId = request.POST.get('mID')
        subId = request.POST.get('sID')

        try:
            if soldStId is not None and mainId is not None:
                soldStk = Auction_SoldStocks.objects.get(pk=soldStId)
                form = AddAuctionSoldStockForm(request.POST, instance=soldStk)

                if form.is_valid():
                    # calculate total price
                    current = Auction_SubStock.objects.get(pk=mainId)
                    netW = current.net_weight
                    total = form.cleaned_data['price'] * netW

                    #update data
                    formObject = form.save(commit=False)
                    formObject.total_price = total
                    formObject.MainID = mainId
                    formObject.SubID = subId
                    formObject.save()

                    messages.success(request, 'Successfully Updated')

                else:
                    messages.error(request, 'Invalid Details')

            else:
                messages.error(request, 'Error main/sub/sold id is null')

        except Exception as e:
            print(e)
            messages.error(request, 'Exception')

    return redirect('stock_sold')


@login_required(login_url='login')
def moveToNotSoldAuctionSubStock(request):

    if request.method == 'POST':
        soldId = request.POST.get('soldID')
        mainID = request.POST.get('mID')
        subID = request.POST.get('sID')

        try:

            if soldId is not None and mainID is not None:
                #delete(inactive) sold stock record
                soldSt = Auction_SoldStocks.objects.get(pk=soldId)
                soldSt.active = 0
                soldSt.save()

                #update current stock
                currentSt = Auction_SubStock.objects.get(pk=mainID)
                currentSt.status = 'Not Sold'
                currentSt.save()

                #add to not sold stock
                notSoldSt = Auction_NotSoldStocks()
                notSoldSt.MainID = mainID
                notSoldSt.SubID = subID
                notSoldSt.save()

                #add to log
                nLog = Auction_NotSoldStocksLog()
                nLog.Description = '<Add_from_sold.Description>: Add Not Sold Stock. | <Main SubStock ID>: '+mainID+' | <Stock Sub ID>: '+subID+''
                nLog.save()

                messages.success(request, 'Sucessfully moved to Not Sold Stock')
                redirect('stock_notsold')

            else:
                messages.error(request, 'Error main/sold id is null')

        except Exception as e:
            print(e)
            messages.error(request, 'Exception')

    return redirect('stock_sold')


@login_required(login_url='login')
def NotSoldStockAdd(request):

    if request.method == 'POST':
        mainId = request.POST.get('mID')
        subId = request.POST.get('sID')

        try:
            if mainId is not None and subId is not None:

                #save data in not sold stock
                notForm = Auction_NotSoldStocks()
                notForm.MainID = mainId
                notForm.SubID = subId
                notForm.save()

                #update status in current stock
                curStock = Auction_SubStock.objects.get(pk=mainId)
                curStock.status = 'Not Sold'
                curStock.save()

                # add data to log
                nLog = Auction_NotSoldStocksLog()
                nLog.Description = '<Add.Description>: Add Not Sold Stock. | <Main SubStock ID>: '+mainId+' | <Stock Sub ID>: '+subId+''
                nLog.save()

                messages.success(request, 'Successfully Added to Not-Sold Stock')
                return redirect('stock_notsold')

            else:
                messages.success(request, 'Main/Sub ID is null')
                return redirect('stock_sales')

        except Exception as e:
            print(e)
            messages.success(request, 'Exception')
            return redirect('stock_sales')

    return redirect('stock_sales')


@login_required(login_url='login')
def notSoldStock(request):

    try:
        notSold = Auction_NotSoldStocks.objects.filter(active=1)
        substocks = Auction_SubStock.objects.filter(status='Not Sold', active=1)
        return render(request, 'auction_notSold.html', {'nStock': notSold, 'subStock':substocks })

    except Exception as e:
        print(e)
        messages.error(request, 'Exception')
        return render(request, 'auction_notSold.html')


@login_required(login_url='login')
def DeleteNotSoldStock(request):

    if request.method == 'POST':
        notStockid = request.POST.get('nID')
        subStockid = request.POST.get('mID')

        if notStockid is not None and subStockid is not None:
            try:
                #add to log
                nLog = Auction_NotSoldStocksLog()
                nLog.Description = '<Delete.Description>: Delete Not Sold Stock. | <Main SubStock ID>: '+subStockid+' | <Not Sold Stock ID>: '+notStockid+''
                nLog.save()

                # delete record from not sold
                nStock = Auction_NotSoldStocks.objects.get(pk=notStockid)
                nStock.delete()

                #update current stock table
                curStock = Auction_SubStock.objects.get(pk=subStockid)
                curStock.status = 'Pending'
                curStock.save()

                messages.success(request, 'Successfully Deleted')
                return redirect('stock_notsold')

            except Exception as e:
                print(e)
                messages.error(request, 'Exception')
                return redirect('stock_notsold')

        else:
            messages.error(request, 'Sub/Not sold id is null')
            return redirect('stock_notsold')


@login_required(login_url='login')
def showAuctionNotSoldLog(request):

    log = Auction_NotSoldStocksLog.objects.all()
    detailsSt = Auction_RePreparedNotSoldStocksDetails.objects.all()

    return render(request, 'auctionNotSoldLog.html', {'Alllog':log, 'Details': detailsSt })


@login_required(login_url='login')
def searchAuctionMainStock(request):

    if request.method == 'GET':

        try:
            text = request.GET.get('sText')
            type = request.GET.get('type')

            #check type
            if type == 'date':
                allCatelogs = Auction_MainStock.objects.filter(Date=text)
                result = Auction_MainStock.objects.filter(Date=text).count()

                messages.success(request, str(result) + ' Results Found')
                return render(request, 'catelogDetails.html', {'MainStocks': allCatelogs})

            elif type == 'month':
                arr = text.split('-',1)
                year = arr[0]
                month = arr[1]
                allCatelogs = Auction_MainStock.objects.filter(Date__year=year, Date__month=month)
                result = Auction_MainStock.objects.filter(Date__year=year, Date__month=month).count()

                messages.success(request, str(result) + ' Results Found')
                return render(request, 'catelogDetails.html', {'MainStocks': allCatelogs})

            elif type == 'year':

                allCatelogs = Auction_MainStock.objects.filter(Date__year=text)
                result = Auction_MainStock.objects.filter(Date__year=text).count()

                messages.success(request, str(result) + ' Results Found')
                return render(request, 'catelogDetails.html', {'MainStocks': allCatelogs})


            elif type == 'subID':
                sid = int(text)
                allCatelogs = Auction_MainStock.objects.filter(SubID=sid)
                result = Auction_MainStock.objects.filter(SubID=sid).count()

                messages.success(request, str(result) + ' Results Found')
                return render(request, 'catelogDetails.html', {'MainStocks': allCatelogs})


            elif type == 'subStockID':
                id = int(text)
                chk = Auction_SubStock.objects.filter(pk=id).exists()

                if chk:
                    subSt = Auction_SubStock.objects.get(pk=id)
                    subID = subSt.SubID

                    allCatelogs = Auction_MainStock.objects.filter(SubID=subID)
                    result = Auction_MainStock.objects.filter(SubID=subID).count()

                    messages.success(request, str(result) + ' Results Found')
                    return render(request, 'catelogDetails.html', {'MainStocks': allCatelogs})

                else:
                    messages.success(request,'No Results Found')

            elif type == 'broker':
                broker = Broker.objects.filter(name=text).exists()

                if broker:
                    broker = Broker.objects.get(name=text)
                    id = broker.id
                    allCatelogs = Auction_MainStock.objects.filter(Broker_id=id)
                    result = Auction_MainStock.objects.filter(Broker_id=id).count()

                    messages.success(request, str(result) + ' Results Found')
                    return render(request, 'catelogDetails.html', {'MainStocks': allCatelogs})

                else:
                    messages.error(request, 'Broker not found')

            else:
                messages.error(request, 'Selection Type Not found')


        except Exception as e:
            print(e)
            messages.error(request, 'Exception.Invalid Details added.')
            return redirect('all_catelog')


    return redirect('all_catelog')


@login_required(login_url='login')
def searchAuctionCurrentSubStock(request):

    if request.method == 'GET':

        try:
            text = request.GET.get('sText')
            type = request.GET.get('type')

            if type == 'mainID':

                chk = Auction_SubStock.objects.filter(pk=text, status='Pending', active=1).exists()

                if chk:
                    stockSub = Auction_SubStock.objects.filter(pk=text, status='Pending', active=1)
                    result = Auction_SubStock.objects.filter(pk=text).count()

                    messages.success(request, str(result) + ' Results Found')
                    return render(request, 'auctionStock_current.html', {'stock': stockSub })

                else:
                    messages.error(request, 'No Data Found')

            elif type == 'subID':

                chk = Auction_SubStock.objects.filter(SubID=text, status='Pending', active=1).exists()

                if chk:
                    stockSub = Auction_SubStock.objects.filter(SubID=text, status='Pending', active=1)
                    result = Auction_SubStock.objects.filter(SubID=text).count()

                    messages.success(request, str(result) + ' Results Found')
                    return render(request, 'auctionStock_current.html', {'stock': stockSub })

                else:
                    messages.error(request, 'No Data Found')


            elif type == 'date':

                chk = Auction_SubStock.objects.filter(date_prepared=text, status='Pending', active=1).exists()

                if chk:
                    stockSub = Auction_SubStock.objects.filter(date_prepared=text, status='Pending', active=1)
                    result = Auction_SubStock.objects.filter(date_prepared=text).count()

                    messages.success(request, str(result) + ' Results Found')
                    return render(request, 'auctionStock_current.html', {'stock': stockSub})

                else:
                    messages.error(request, 'No Data Found')


            elif type == 'month':
                arr = text.split('-',1)
                year = arr[0]
                month = arr[1]

                chk = Auction_SubStock.objects.filter(date_prepared__year=year, date_prepared__month=month, status='Pending', active=1).exists()

                if chk:
                    stockSub = Auction_SubStock.objects.filter(date_prepared__year=year, date_prepared__month=month, status='Pending', active=1)
                    result = Auction_SubStock.objects.filter(date_prepared__year=year, date_prepared__month=month, status='Pending', active=1).count()

                    messages.success(request, str(result) + ' Results Found')
                    return render(request, 'auctionStock_current.html', {'stock': stockSub})

                else:
                    messages.error(request, 'No Data Found')

            elif type == 'year':
                chk = Auction_SubStock.objects.filter(date_prepared__year=text,status='Pending', active=1).exists()

                if chk:
                    stockSub = Auction_SubStock.objects.filter(date_prepared__year=text,status='Pending', active=1)
                    result = Auction_SubStock.objects.filter(date_prepared__year=text,status='Pending', active=1).count()

                    messages.success(request, str(result) + ' Results Found')
                    return render(request, 'auctionStock_current.html', {'stock': stockSub})

                else:
                    messages.error(request, 'No Data Found')

            else:
                messages.error(request, 'Invalid Type')

        except Exception as e:
            print(e)
            messages.success(request, 'Exception: Invalid Details')

    return redirect('stock_sales')


@login_required(login_url='login')
def searchAuctionSoldStock(request):

    if request.method == 'GET':

        try:
            text = request.GET.get('sText')
            type = request.GET.get('type')
            substocks = Auction_SubStock.objects.filter(status='Sold', active=1)

            if type == 'mainID':
                chk = Auction_SoldStocks.objects.filter(MainID=text, active=1).exists()

                if chk:
                    sold = Auction_SoldStocks.objects.filter(MainID=text,active=1)
                    count = Auction_SoldStocks.objects.filter(MainID=text,active=1).count()

                    messages.success(request, str(count) + ' Results found')
                    return render(request, 'auction_soldStock.html', {'soldStocks': sold, 'subStocks': substocks})

                else:
                    messages.error(request, 'No result found')

            elif type == 'subID':
                chk = Auction_SoldStocks.objects.filter(SubID=text, active=1).exists()

                if chk:
                    sold = Auction_SoldStocks.objects.filter(SubID=text, active=1)
                    count = Auction_SoldStocks.objects.filter(SubID=text, active=1).count()

                    messages.success(request, str(count)+' Results found')
                    return render(request, 'auction_soldStock.html', {'soldStocks': sold, 'subStocks': substocks})

                else:
                    messages.error(request, 'No result found')

            elif type == 'dateSold':
                chk = Auction_SoldStocks.objects.filter(sold_Date=text, active=1).exists()

                if chk:
                    sold = Auction_SoldStocks.objects.filter(sold_Date=text, active=1)
                    count = Auction_SoldStocks.objects.filter(sold_Date=text, active=1).count()

                    messages.success(request, str(count)+' Results found')
                    return render(request, 'auction_soldStock.html', {'soldStocks': sold, 'subStocks': substocks})

                else:
                    messages.error(request, 'No result found')

            elif type == 'month':
                arr = text.split('-',1)
                year = arr[0]
                month = arr[1]

                chk = Auction_SoldStocks.objects.filter(sold_Date__year=year, sold_Date__month=month, active=1).exists()

                if chk:
                    sold = Auction_SoldStocks.objects.filter(sold_Date__year=year, sold_Date__month=month, active=1)
                    count = Auction_SoldStocks.objects.filter(sold_Date__year=year, sold_Date__month=month, active=1).count()

                    messages.success(request, str(count)+' Results found')
                    return render(request, 'auction_soldStock.html', {'soldStocks': sold, 'subStocks': substocks})

                else:
                    messages.error(request, 'No result found')

            elif type == 'year':

                chk = Auction_SoldStocks.objects.filter(sold_Date__year=text, active=1).exists()

                if chk:
                    sold = Auction_SoldStocks.objects.filter(sold_Date__year=text, active=1)
                    count = Auction_SoldStocks.objects.filter(sold_Date__year=text, active=1).count()

                    messages.success(request, str(count) + ' Results found')
                    return render(request, 'auction_soldStock.html', {'soldStocks': sold, 'subStocks': substocks})

                else:
                    messages.error(request, 'No result found')

            else:
                messages.error(request, 'Invalid Type')

        except Exception as e:
            print(e)
            messages.success(request, 'Exception: Invalid Details')

    return redirect('stock_sold')


#Production Analysis--------------------------------------------------------------------------------------------


@login_required(login_url='login')
def productionAnalysisHome(request):

    return render(request, 'finalProductAnalysis.html')


class ReportAuctionSoldStock(View):
    def get(self, request, *args, **kwargs):

        substocks = Auction_SubStock.objects.filter(status='Sold', active=1)

        text = request.GET.get('input')
        type = request.GET.get('type')

        sold = AuctionSoldStockDetails(text, type)

        if sold['stock'] == -1 :
            messages.error(request,'Exception(Invalid Details')
            return redirect('production_analysis')

        elif sold['stock'] == -99:
            messages.error(request,'Invalid Type')
            return redirect('production_analysis')

        elif sold['stock'] == 0:
            messages.error(request,'No results Found')
            return redirect('production_analysis')

        else:
            # template = get_template('AuctionStockSoldStockReoprt.html')
            # html = template.render(context)

            #calculations
            calc = calculateTotalAuction(sold['stock'])

            context = {
                'soldStocks': sold,
                'subStocks': substocks,
                'calculations': calc,
                'type': type,
                'text': text,
               }

            pdf = finalProductionAuction_render_topdf('AuctionStockSoldStockReoprt.html', context)

            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                return response

            else:
                messages.error(request, 'Error Pdf')
                return redirect('production_analysis')



# class ReportAuctionNotSoldStock(View):
#     def get(self, request , *args, **kwargs):
#         return None


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
