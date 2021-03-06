from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Ambrosia_Project.forms import *
from Ambrosia_Project.common_utills.auctionStockUtills import *
from django.http import HttpResponse
from Ambrosia_Project.common_utills.utils import render_to_pdf


@login_required(login_url='login')
def NavigateToInventory(request):
    form = AddInventoryForm()
    if request.method == 'POST':
        form = AddInventoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Inventory details saved successfully')
                return redirect('NavigateToPreInv')
            except:
                pass

        else:
            messages.error(request, "Invalid Details")


    var = {'form': form}
    return render(request, 'LeafInventory_templates/add_inventory.html', var)


@login_required(login_url='login')
def NavigateToPrevInv(request):
    leaf = LeafInventory.objects.all()
    return render(request, 'LeafInventory_templates/View_pre_inv.html', {'leaf': leaf})


@login_required(login_url='login')
def NavigateToUpdateInv(request):

    if request.method == 'POST':
        inv_ID = request.POST.get('lid')

        if inv_ID is not None:
            try:
                leaf = LeafInventory.objects.get(id=inv_ID)
                form = AddInventoryForm(instance=leaf)
                return render(request, 'LeafInventory_templates/update_inventory.html', {'form': form, 'lid':inv_ID})

            except Exception as e:
                print(e)

        else:
            messages.error(request, "Inv id is null")

    else:
        #method is not post
        pass


    return render(request, 'LeafInventory_templates/View_pre_inv.html')



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

    return render(request, 'DailyProduction_templates/Add_daily_product.html', var)


@login_required(login_url='login')
def addMainFinalProduction(request):

    if request.method == 'POST':
        sid = request.POST.get('sID')

        # calculate total weight
        total = 0
        allProduct = Final_product_sub.objects.filter(subID=sid)

        for product in allProduct:
            total = total + product.gradeWeight

        form = AddMainProductForm(request.POST)

        if form.is_valid():
            mainObj = form.save(commit=False)
            mainObj.subID = sid
            mainObj.totalWeight = total
            mainObj.save()

            messages.success(request, "Successfully Saved Data")
            return redirect('NavigateToCustomDailyProd')

        else:
            messages.error(request, "invalid")


    return redirect('final_production_home')


@login_required(login_url='login')
def deleteSubProd(request):

    if request.method == 'POST':
        sID = request.POST.get('id')

        if sID is not None:

            try:
                subProd = Final_product_sub.objects.get(id=sID)

                #update main prod
                mainProdID = subProd.subID
                mainProd = Final_product_Main.objects.get(subID=mainProdID)

                mainProd.totalWeight = mainProd.totalWeight - subProd.gradeWeight
                mainProd.save()

                #delete sub prod
                subProd.delete()

                subProuctChk = Final_product_sub.objects.filter(subID=mainProdID)

                if len(subProuctChk) < 1:
                    mainProd.delete()


                messages.success(request, 'Successfully Deleted')
                return redirect('NavigateToCustomDailyProd')

            except Exception as e:
                print(e)

    return redirect('NavigateToCustomDailyProd')


@login_required(login_url='login')
def NavigateToCustomDailyProd(request):
    prod = Final_product_Main.objects.all()
    return render(request, 'DailyProduction_templates/View_Daily_production.html', {'prod':prod})


@login_required(login_url='login')
def NavigateToViewProduct(request):

    if request.method == 'POST':
        sid = request.POST.get('id')

        product = Final_product_sub.objects.filter(subID=sid)
        mainProd = Final_product_Main.objects.get(subID=sid)
        date = mainProd.date

    return render(request, 'DailyProduction_templates/sub_final_product_view.html', {'products': product, 'date': date})


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
    return render(request, 'LeafInventory_templates/View_pre_inv.html')


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
                    messages.error(request, "Invalid Details")

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
                messages.success(request, 'Tea grade Saved successfully')
                return redirect('NavigateToTeaGrades')
            except:
                pass

    grade = TeaGrades.objects.all()

    var = {'form': form,
           'grade': grade}

    return render(request, 'DailyProduction_templates/TeaGrades.html', var)


def DeleteGrade(request):
    grade = request.POST.get('grade')

    if request.method == 'POST' and grade is not None:
        gradeT = TeaGrades.objects.get(id=grade)
        gradeT.delete()

    return redirect('NavigateToTeaGrades')


@login_required(login_url='login')
def NavigateToInvReport(request):

    if request.method == 'POST':
        leafID = request.POST.get('leafID')

        leaf = LeafInventory.objects.get(id=leafID)

        context = {
           'leaf':leaf,
        }

        pdf = render_to_pdf('LeafInventory_templates/inventoryPDF.html', context)

        return HttpResponse(pdf, content_type='application/pdf')


    return redirect('NavigateToPreInv')