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

def SalesPriceTableFGS(request):

    return render(request, 'SalesPriceTableFGS.html')