from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Ambrosia_Project.forms import *

from Ambrosia_Project.forms import CreateUserForm
from django.contrib.auth.models import User
from Ambrosia_Project.models import *

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


#Supplier Management------------------------------------------------------------------------------------------


#Navigate from Admin home to Registered Suppliers List
@login_required(login_url='login')
def to_reg_suppliers(request):

    return render(request, 'AllRegisteredSuppliers.html')



#Leaf Inventory-------------------------------------------------------------------------------------------


@login_required(login_url='login')
def NavigateToInventory(request):
    return render(request, 'add_inventory.html')


#Final production -------------------------------------------------------------------------------------------

#Daily Production------------------------------------------------------------------------------------------


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
