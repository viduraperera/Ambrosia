from django.shortcuts import render, redirect
from Ambrosia_Project.forms import *
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Ambrosia_Project.common_utills.salesutills import *


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
                messages.success(request, 'Invalid Quantity')

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
            if transaction:
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

                messages.error(request, 'Transactions are not Founded')
                return redirect('SalesHomeIncome')

        else:
            return redirect('SalesHomeIncome')

class GeneratePDFInvoiceAnnually(View):
    def get(self, request, *args, **kwargs):

        year = request.GET.get('year')
        transaction = Transactions.objects.filter(dateTime__year=year)

        total = 0
        if transaction:
            for tr in transaction:
                total = total + tr.total_Price

            data = {
                'trans': transaction,
                'total': total,
                'year': year,
                }

            pdf = render_to_pdf('TeaShopSales_Templates/SalesHomeAnnuallyIncome.html', data)

            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                return response
            else:
                messages.error(request, 'Error Pdf')
        else:
            messages.error(request, 'Transactions are not Founded')
            return redirect('SalesHomeIncome')

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
