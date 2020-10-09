from django.shortcuts import render, redirect
from django.http import HttpResponse
from xhtml2pdf import pisa

from Ambrosia_Project.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Ambrosia_Project.models import *
from Ambrosia_Project.forms import *
from django.http import HttpResponse
from django.views.generic import View
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from Ambrosia_Project.utils import render_to_pdf


# Create your views here.

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
        return render(request, 'updateUser.html', {'UserDetails': user, 'form': form})

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


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def factoryhome(request):
    return render(request, 'factoryhome.html')


@login_required(login_url='login')
def teashopHomepage (request):
    return render(request, 'teashophome.html')


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

#------------Ravija------------------------------------------------------------------------------------------------------------

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
def NavigateToCurrentProduct(request):
    return render(request, 'DailyProduction_templates/Current_product.html')


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
