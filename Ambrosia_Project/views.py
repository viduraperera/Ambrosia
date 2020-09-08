from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ambrosia_Project.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
def teashopHomepage (request):

    return render(request, 'teashophome.html')

@login_required(login_url='login')
def EmployeeHome (request):

    return render(request, 'EmployeeManagement.html')

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
        pword =request.POST.get('pwd')

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

    messages.error(request, "Error.Can't Update Details.")
    return redirect('view_all_users')


@login_required(login_url='login')
def DeleteUser(request):

    uname = request.POST.get('uname')

    if request.method == 'POST' and uname != None:
        user = User.objects.get(username=uname)
        user.delete();
        messages.success(request, "User Deleted Successfully")
        return redirect('view_all_users')

    else:
        messages.error(request, "Can't Delete User.")
        return redirect('view_all_users')

    messages.error(request, "Error.Can't Delete User.")
    return redirect('view_all_users')

@login_required(login_url='login')
def FinalProduction(request):

    return render(request, 'finalproductionhome.html')

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