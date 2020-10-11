from django.shortcuts import render, redirect
from Ambrosia_Project.forms import *
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Ambrosia_Project.common_utills.salesutills import *


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

                    # save stock details
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
def inventorymonthlyreport (request):
    return render(request, 'TeaShopInventory_Templates/inventorymonthlyreport.html')


@login_required(login_url='login')
def inventoryannualreport (request):
    return render(request, 'TeaShopInventory_Templates/inventoryannualreport.html')


class GenerateStockMothlyReport(View):
    def get(self, request, *args, **kwargs):

        month = request.GET.get('month')
        year = request.GET.get('year')

        if len(month) == 2 and len(year) == 4:

            packets = AddPackets.objects.filter(date__month=month, date__year=year)
            prodCat = CategoryProduct.objects.all()
            data = {
                'Packets': packets,
                'prod': prodCat
            }
            pdf = render_to_pdf('TeaShopInventory_Templates/inventorymonthlyreport.html', data)

            return HttpResponse(pdf, content_type='application/pdf')

        else:
            return redirect('inventoryreports')


class GenerateStockAnnualReport(View):
    def get(self, request, *args, **kwargs):

        year = request.GET.get('year')

        if len(year) == 4:

            packets = AddPackets.objects.filter(date__year=year)
            prodCat = CategoryProduct.objects.all()
            data = {
                'Packets': packets,
                'prod': prodCat
            }
            pdf = render_to_pdf('TeaShopInventory_Templates/inventoryannualreport.html', data)

            return HttpResponse(pdf, content_type='application/pdf')

        else:
            return redirect('inventoryreports')

