from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ambrosia_Project.forms import *
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Ambrosia_Project.models import *
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
    #
    # messages.error(request, "Error.Can't Delete User.")
    # return redirect('view_all_users')

#--------------------------------------------------------------------------------------------



@login_required(login_url='login')
def inventoryhome (request):
    return render(request, 'TeaShopInventory_Templates/../templates/inventoryhome.html')


@login_required(login_url='login')
def addCategoryProduct(request):

    form = AddcategoryProductForm()

    if request.method == 'POST':

        form = AddcategoryProductForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully Added")
                return redirect('addCategoryProduct')

            else:
                messages.error(request, 'Error Invalid Details')

        except Exception as e:
            print(e)

    cprod = CategoryProduct.objects.all()

    return render(request, 'TeaShopInventory_Templates/addCategoryProduct.html', {'form': form, 'c_products': cprod})


@login_required(login_url='login')
def viewCategoryProduct(request):

    if request.method == 'POST':
        cpID = request.POST.get('cpID')

        cat_product = CategoryProduct.objects.get(id=cpID)
        form = AddcategoryProductForm(instance=cat_product)

        return render(request, 'TeaShopInventory_Templates/viewCategoryProduct.html', {'cpForm': form, 'cpID': cpID})

    return redirect('addCategoryProduct')


@login_required(login_url='login')
def updateategoryProduct(request):

    if request.method == 'POST':
        cpID = request.POST.get('cpID')

        if cpID is not None:
            try:

                cat_product = CategoryProduct.objects.get(id=cpID)
                form = AddcategoryProductForm(request.POST, instance=cat_product)

                if form.is_valid():
                    form.save()
                    messages.success(request, "Successfully Updated")
                    return redirect('addCategoryProduct')

                else:
                    messages.error(request, "Invalid Details")

            except Exception as e:
                print(e)

        else:
            messages.error(request, "CPID is null")


    return redirect('addCategoryProduct')


@login_required(login_url='login')
def deleteCategoryProduct(request):

    if request.method == 'POST':
        prID = request.POST.get('cpID')

        if prID is not None:

            try:
                produtCat = CategoryProduct.objects.get(id=prID)
                produtCat.delete()
                messages.success(request, 'Sucessfully Deleted')
                return redirect('addCategoryProduct')

            except Exception as e:
                print(e)

        else:
            messages.error(request, 'Category Product ID is null')


    return redirect('addCategoryProduct')


@login_required(login_url='login')
def viewpackets(request):

    packets = AddPackets.objects.all()
    prodCat = CategoryProduct.objects.all()

    return render(request, 'TeaShopInventory_Templates/viewpackets.html', {'Packets': packets, 'prod': prodCat})

def inventoryhome(request):
    return render(request, 'inventoryhome.html')

@login_required(login_url='login')
def addteapackets (request):

    formA = AddTeaPacketsForm()

    if request.method == 'POST':

        formA = AddTeaPacketsForm(request.POST)

        if formA.is_valid():

            try:
                categoryID = formA.cleaned_data['categoryProductID'].id
                packets = formA.cleaned_data['noOfPackets']

                # savepacket details
                formA.save()

                categoryProduct = CategoryProduct.objects.get(id=categoryID)
                weight = categoryProduct.weight
                category = categoryProduct.category

                stock = Stock.objects.filter(weight=weight, category=category)

                if len(stock) < 1 :

                    # savae stock details
                    stock = Stock()
                    stock.category = category
                    stock.weight = weight
                    stock.available_stock = packets
                    stock.save()

                    messages.success(request, 'Successfullly added')
                    return redirect('viewpackets')

                else:
                    # update stock details
                    stock = Stock.objects.get(weight=weight, category=category)
                    prevPkts = stock.available_stock
                    stock.available_stock = prevPkts + packets

                    stock.save()

                    messages.success(request, 'Successfullly added')
                    return redirect('viewpackets')


            except Exception as e:
                print(e)

        else:
            messages.error(request, 'Invalid Details')

    return render(request, 'TeaShopInventory_Templates/addteapackets.html', {'form': formA})


@login_required(login_url='login')
def editpackets (request):

    if request.method == 'POST':
        packetId = request.POST.get('pid')

        if packetId is not None:

            try:
                packet = AddPackets.objects.get(pk=packetId)
                pktID = packet.categoryProductID.id
                categoryProd = CategoryProduct.objects.get(id=pktID)
                category = categoryProd.category
                weight = categoryProd.weight

                det = {
                    'category': category,
                    'weight': weight,
                    'packet': packet
                }

                return render(request, 'TeaShopInventory_Templates/editpackets.html', det)

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'TeaShopInventory_Templates/viewpackets.html')


@login_required(login_url='login')
def updatePackets(request):

    if request.method == 'POST':
        pktId = request.POST.get('packetID')
        pktsNew = int(request.POST.get('noPkts'))

        if pktId is not None:
            try:

                if pktsNew > 0:

                    #calculations
                    packet = AddPackets.objects.get(pk=pktId)
                    oldNoPkts = packet.noOfPackets

                    cpID = packet.categoryProductID.id
                    catProduct = CategoryProduct.objects.get(id=cpID)

                    stock = Stock.objects.get(category=catProduct.category, weight=catProduct.weight)
                    currentPkts = stock.available_stock

                    newStock = currentPkts + pktsNew - oldNoPkts

                    #db
                    #update packet table
                    packet.noOfPackets = pktsNew
                    packet.save()

                    #update stock
                    stock.available_stock = newStock
                    stock.save()

                    messages.success(request, 'Successfully Updated')
                    return redirect('viewpackets')


                else:
                    #invalid
                    messages.error(request, 'Invalid No of Packets')

            except Exception as e:
                print(e)

        else:
            pass

    return redirect('viewpackets')


@login_required(login_url='login')
def deletepackets(request):

    packetsid = request.POST.get('deleteid')

    if request.method == 'POST' and packetsid is not None:

        try:
            packets = AddPackets.objects.get(id=packetsid)

            noOfPkts = packets.noOfPackets

            catID = packets.categoryProductID_id
            category_Product = CategoryProduct.objects.get(id=catID)

            weight = category_Product.weight
            category = category_Product.category

            stock = Stock.objects.get(weight=weight, category=category)
            prevpkts = stock.available_stock

            if stock is not None:
                stock.available_stock = prevpkts - noOfPkts
                stock.save()

                packets.delete()
                messages.success(request, 'Deleted Successfully')

            else:
                messages.error(request, 'Error')

        except Exception as e:
            print(e)

    return redirect('viewpackets')


@login_required(login_url='login')
def availableStock (request):

    stock = Stock.objects.all()

    return render(request, 'TeaShopInventory_Templates/availbleStock.html', {'stock': stock})


@login_required(login_url='login')
def inventoryreports (request):
    return render(request, 'TeaShopInventory_Templates/inventoryreports.html')


@login_required(login_url='login')
def iweekly (request):
    return render(request, 'TeaShopInventory_Templates/iweekly.html')


@login_required(login_url='login')
def inventorymonthlyreport (request):
    return render(request, 'TeaShopInventory_Templates/inventorymonthlyreport.html')


@login_required(login_url='login')
def inventoryannualreport (request):
    return render(request, 'TeaShopInventory_Templates/inventoryannualreport.html')

#-----------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
def SalesHomeIncome(request):
    return render(request, 'TeaShopSales_Templates/SalesHomeIncome.html')


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

                stock = Stock.objects.get(weight=weight, category=cat)

                if stock:

                    availablePkts = stock.available_stock


                    if availablePkts >= qty:

                        stock.available_stock = availablePkts - qty
                        stock.save()

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
                        messages.success(request, 'Maximum Stock Exceeded')





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

    return render(request, 'TeaShopSales_Templates/SalesCreateInvoice.html', var)


# createinvoicepageDeletion

@login_required(login_url='login')
def BillRowDelete(request):
    item = request.POST.get('rowDelete')

    if request.method == 'POST' and item != None:

        rowDelete = BillItems.objects.get(pk=item)

        cat = rowDelete.itemname
        weight = rowDelete.weight
        qty = rowDelete.Quantity

        stock = Stock.objects.get(weight=weight, category=cat)

        if stock:
            availablePkts = stock.available_stock
            stock.available_stock = availablePkts + qty
            stock.save()

        #delete from bill item
        rowDelete.delete()

    return redirect('SalesCreateInvoice')


# read
@login_required(login_url='login')
def SalesViewBill(request):

    if request.method == 'POST':

        invId = request.POST.get('invID')
        tID = request.POST.get('trID')

        bills = BillItems.objects.filter(invoice_id=invId)
        trancsaction = Transactions.objects.get(id=tID)

        return render(request, 'TeaShopSales_Templates/SalesViewBill.html', {'billItems': bills , 'viewT': trancsaction})

    else:
        return redirect('SalesTransaction')


# delete
# @login_required(login_url='login')
# def Vdelete(request):
#     invoice = request.POST.get('invoiceid')
#     if request.method == 'POST' and invoice != None:
#         invoiceid = BillItems.objects.get(id=invoice)
#         invoiceid.delete()
#
#     return redirect('SalesViewBill')


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

    return render(request, 'TeaShopSales_Templates/SalesTransaction.html', {'tForm': tl})


@login_required(login_url='login')
def SalesPriceTable(request):
    form = priceTableForm()

    if request.method == "POST":
        form = priceTableForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Sucessfully Added Price')
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

    return render(request, 'TeaShopSales_Templates/SalesPriceTable.html', {'prices': priceTable, 'form': form})


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
                    print(priceForm.errors)

                    messages.success(request, 'Invalid Details')


            except Exception as e:

                print(e)

                messages.success(request, 'Exception:')

            else:
                messages.success(request, 'Invalid Details')
                print(priceForm.errors)

            return render(request, 'TeaShopSales_Templates/ShopPriceTableUpdate.html', {'PriceTableForm': priceForm, 'PID': pid})

    else:

        return redirect('SalesPriceTable')

    return render(request, 'TeaShopSales_Templates/ShopPriceTableUpdate.html', {'prices', priceForm})


@login_required(login_url='login')
def ShopPriceTableUpdate(request):
    if request.method == 'POST':
        pid = request.POST.get('priceID')

        if pid is not None:
            try:
                priceTable = Price_Table.objects.get(pk=pid)
                priceForm = priceTableForm(instance=priceTable)
                # messages.success(request, 'Sucessfully Upadted.')
                return render(request, 'TeaShopSales_Templates/ShopPriceTableUpdate.html', {'pForm': priceForm, 'pid': pid})

            except Exception as e:
                print(e)
                return redirect('SalesPriceTable')

        else:
            pass

    else:
        pass

class GeneratePDFInvoiceMonthly(View):
    def get(self, request, *args, **kwargs):

        # template = get_template(('SalesWeeklyReport.html'))

        month = request.GET.get('month')
        year = request.GET.get('year')

        if len(month) == 2 and len(year) == 4:

            transaction = Transactions.objects.filter(dateTime__month=month, dateTime__year=year)

            total = 0

            for tr in transaction:
                total = total + tr.total_Price

            data = {
                'trans': transaction,
                'total': total,
                'year': year,
                'month': month

            }

            pdf = render_to_pdf('TeaShopSales_Templates/SalesWeeklyReport.html', data)

            return HttpResponse(pdf, content_type='application/pdf')

        else:
            return redirect('SalesHomeIncome')

class GeneratePDFInvoiceAnnually(View):
    def get(self, request, *args, **kwargs):

        year = request.GET.get('year')



        transaction = Transactions.objects.filter(dateTime__year=year)

        total = 0

        for tr in transaction:
            total = total + tr.total_Price

        data = {
            'trans': transaction,
            'total': total,
                'year': year,


            }

        pdf = render_to_pdf('TeaShopSales_Templates/SalesHomeAnnuallyIncome.html', data)

        return HttpResponse(pdf, content_type='application/pdf')

class GenerateBill(View):
    def get(self, request, *args, **kwargs):

        if request.method == 'GET':

            invID = request.GET.get('invID')
            tID = request.GET.get('trID')

            bills = BillItems.objects.filter(invoice_id=invID)
            trancsaction = Transactions.objects.get(id=tID)

            data = {'billItems': bills,
                    'viewT': trancsaction}

            pdf = render_to_pdf('TeaShopSales_Templates/SalesBill.html', data)

            if pdf:
                return HttpResponse(pdf, content_type='application/pdf')
            return HttpResponse("Not found ")

        return redirect('SalesTransaction')
