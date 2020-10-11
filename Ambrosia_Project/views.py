from django.shortcuts import render, redirect
from Ambrosia_Project.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

#Home Navigations------------------------------------------------------------------------------------------

@login_required(login_url='login')
def home(request):

    return render(request, 'common_templates/home.html')

@login_required(login_url='login')
def factoryhome(request):
    return render(request, 'common_templates/factoryhome.html')


@login_required(login_url='login')
def teashopHomepage (request):

    return render(request, 'common_templates/teashophome.html')

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
    return render(request, 'common_templates/registration.html', context)


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
                return render(request, 'common_templates/login.html')

    return render(request, 'common_templates/login.html')


@login_required(login_url='login')
def view_AllUsers(request):

    array = User.objects.all()
    return render(request, 'common_templates/ViewAllUsers.html', {'Users': array})


@login_required(login_url='login')
def ShowUser(request):

    uname = request.POST.get("uname")

    user = User.objects.get(username=uname)
    form = CreateUserForm(instance=user)

    if user is not None:
        return render(request, 'common_templates/updateUser.html', {'UserDetails': user, 'form': form})

    else:
        #user not found
        pass

    return render(request, 'common_templates/ViewAllUsers.html')


@login_required(login_url='login')
def UpdateUser(request):

    if request.method == 'POST':
        uname = request.POST.get('un')

        try:
            user = User.objects.get(username=uname)
            userFrom = CreateUserForm(request.POST, instance=user)

            if userFrom.is_valid():
                userFrom.save()
                messages.success(request, "User Details Updated Successfully")
                return redirect('view_all_users')

            else:
                print(userFrom.errors)
                messages.error(request, "Invalid Details")

        except Exception as e:
            print(e)
            messages.error(request, "Can't Update Details.")

    return redirect('view_all_users')


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

