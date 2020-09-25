from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ambrosia_Project.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Ambrosia_Project.models import *
from Ambrosia_Project.forms import *
from Ambrosia_Project.salesutills import *


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

    users = User.objects.all()

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
            user.save()
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


# add
@login_required(login_url='login')
def SalesCreateInvoice(request):

    form = billItemsForm()
    bid = generateinvoiceid()


    if request.method == "POST":
        form = billItemsForm(request.POST)
        try:
            if form.is_valid():
                cat = form.cleaned_data['itemname']
                weight = form.cleaned_data['weight']
                qty = form.cleaned_data['Quantity']

                calDet = {
                    'qty': qty,
                    'weight': weight,
                    'cat': cat,
                }

                result = calculateTotalprice(calDet)

                totalPrice = result['totalPrice']
                itemPrice = result['itemPrice']

                invform = form.save(commit=False)
                invform.invoice_id = bid
                invform.itemPrice = itemPrice
                invform.price = totalPrice
                invform.save()
                messages.success(request, 'Sucessfully Added Bill Item Details')
                return redirect('SalesCreateInvoice')

            else:
                print(form.errors)
                messages.success(request, 'Invalid Details')

        except Exception as e:
            print(e)
            messages.success(request, 'Exception:')
            return redirect('SalesCreateInvoice')


    # transactiontotalcal
    invoicelist = BillItems.objects.filter(invoice_id=bid)

    var = {'billForm': form,
           'bid': bid,
           'Invoicelist': invoicelist
           }

    return render(request, 'SalesCreateInvoice.html', var)


# createinvoicepageDeletion

@login_required(login_url='login')
def BillRowDelete(request):
    item = request.POST.get('rowDelete')

    if request.method == 'POST' and item != None:
        rowDelete = BillItems.objects.get(pk=item)
        rowDelete.delete()

    return redirect('SalesCreateInvoice')


# read
@login_required(login_url='login')
def SalesViewBill(request):

    # if request.method == 'POST':
    #     viewid = request.POST.get('bid')
    #
    #     Viewbill = viewbill(viewid)
    #
    #     try:
    #         transaction = Transactions()
    #         transaction.invoice_id = viewid
    #         transaction.id = Viewbill
    #         transaction.save()
    #         messages.success(request, 'Sucessfully Created bill')
    #         return redirect('SalesTransaction')
    #
    #     except Exception as e:
    #         print(e)


    var = Transactions.objects.filter()
    arr = BillItems.objects.filter()



    return render(request, 'SalesViewBill.html', {'saleInvoice': arr,'viewT': var, })


# delete
@login_required(login_url='login')
def Vdelete(request):
    invoice = request.POST.get('invoiceid')
    if request.method == 'POST' and invoice != None:
        invoiceid = BillItems.objects.get(id=invoice)
        invoiceid.delete()

    return redirect('SalesViewBill')


@login_required(login_url='login')
def SalesTransaction(request):


    if request.method == 'POST':
        transactionID = request.POST.get('bid')

        totalprice = transactioncalTotal(transactionID)

        try:
            transaction = Transactions()
            transaction.invoice_id = transactionID
            transaction.total_Price = totalprice
            transaction.save()
            messages.success(request, 'Sucessfully Created bill')
            return redirect('SalesTransaction')


        except Exception as e:
            print(e)

    tl = Transactions.objects.all()

    return render(request, 'SalesTransaction.html', {'tForm': tl})


#
#
#
#
# edit
# update
# readpriceTable

@login_required(login_url='login')
def SalesPriceTable(request):
    form = priceTableForm()

    if request.method == "POST":
        form = priceTableForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Sucessfully Added Bill Item Details')
                return redirect('SalesPriceTable')



            else:
                print(form.errors)
                messages.success(request, 'Invalid Details')
                pass

        except Exception as e:
            print(e)
            messages.success(request, 'Exception:')
            return redirect('SalesCreateInvoice')

    priceTable = Price_Table.objects.all()

    return render(request, 'SalesPriceTable.html', {'prices': priceTable, 'form': form})


@login_required(login_url='login')
def ShopPriceTableEdit(request):
    if request.method == 'POST':

        priceForm = priceTableForm(request.POST)
        pid = request.POST.get('id')

        if priceForm.is_valid():

            try:
                price = Price_Table.objects.get(pk=pid)
                messages.success(request, 'Sucessfully Upadted.')

                if price is not None:
                    price_form = priceTableForm(request.POST, instance=price)
                    price_form.save()

                    return redirect('SalesPriceTable')

                else:
                    pass


            except Exception as e:
                print(e)

            else:
                messages.success(request, 'Invalid Details')
                print(priceForm.errors)

            return render(request, 'ShopPriceTableUpdate.html', {'PriceTableForm': priceForm, 'PID': pid})

    else:

        return redirect('SalesPriceTable')

    return render(request, 'ShopPriceTableUpdate.html', {'prices', priceForm})


@login_required(login_url='login')
def ShopPriceTableUpdate(request):
    if request.method == 'POST':
        pid = request.POST.get('priceID')

        if pid is not None:
            try:
                priceTable = Price_Table.objects.get(pk=pid)
                priceForm = priceTableForm(instance=priceTable)
                # messages.success(request, 'Sucessfully Upadted.')
                return render(request, 'ShopPriceTableUpdate.html', {'pForm': priceForm, 'pid': pid})

            except Exception as e:
                print(e)
                return redirect('SalesPriceTable')

        else:
            pass

    else:
        pass


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
