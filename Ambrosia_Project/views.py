from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ambrosia_Project.forms import CreateUserForm, AddTeaPacketsForm, PreOrderLevelForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
from Ambrosia_Project.models import addPackets, preorder


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
def inventoryhome (request):
    return render(request, 'inventoryhome.html')


@login_required(login_url='login')
def addteapackets (request):
    return render(request, 'addteapackets.html')


@login_required(login_url='login')
def inventoryreports (request):
    return render(request, 'inventoryreports.html')


@login_required(login_url='login')
def iweekly (request):
    return render(request, 'iweekly.html')


@login_required(login_url='login')
def inventorymonthlyreport (request):
    return render(request, 'inventorymonthlyreport.html')


@login_required(login_url='login')
def inventoryannualreport (request):
    return render(request, 'inventoryannualreport.html')


@login_required(login_url='login')
def viewpackets(request):

    packets = addPackets.objects.all()

    return render(request, 'viewpackets.html', {'Packets': packets})


@login_required(login_url='login')
def addteapackets (request):

    formA = AddTeaPacketsForm()

    if request.method == 'POST':

        formA = AddTeaPacketsForm(request.POST)

        if formA.is_valid():
            try:
                formA.save()
                messages.success(request, 'Successfullly added')
                return redirect('viewpackets')
            except Exception as e:
                #pass
                print(e)
                messages.success(request, 'Exception:'+e)
                # return redirect('viewpackets')
        else:
            # form method is not valid
            # print(formA.errors)
            # messages.success(request, 'Invalid Details')
            pass

    return render(request, 'addteapackets.html', {'form': formA})


@login_required(login_url='login')
def editpackets (request):

    if request.method == 'POST':
        packetId = request.POST.get('pid')

        if packetId is not None:

            try:
                packet = addPackets.objects.get(pk=packetId)
                form = AddTeaPacketsForm(instance=packet)

                return render(request, 'editpackets.html', {'pForm': form, 'PID': packetId})

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'viewpackets.html')


@login_required(login_url='login')
def updatePackets(request):

    if request.method == 'POST':
        pktId = request.POST.get('pktid')

        if pktId is not None:
            packet = addPackets.objects.get(pk=pktId)
            pform = AddTeaPacketsForm(request.POST, instance=packet)

            if pform.is_valid():
                pform.save()
                messages.success(request, 'Edited Successfully')
                return redirect('viewpackets')

            else:
                #invalid
                return render(request, 'editpackets.html', {'pForm': pform, 'PID': pktId})

        else:
            pass

    return render(request, 'viewpackets.html')


@login_required(login_url='login')
def deletepackets(request):
    packetsid = request.POST.get('deleteid')

    if request.method == 'POST' and packetsid is not None:
        packets = addPackets.objects.get(id=packetsid)
        packets.delete()
        messages.success(request, 'Deleted Successfully')
    return redirect('viewpackets')


@login_required(login_url='login')
def preorderlevel(request):

    all = preorder.objects.all()
    bopf = all.filter(category='BOPF')
    dust1 = all.filter(category='DUST 1')
    dust2 = all.filter(category='DUST 2')
    fgs = all.filter(category='FGS')

    form = PreOrderLevelForm()

    var = {
        'Bopf': bopf,
        'DUST1': dust1,
        'DUST2': dust2,
        'FGS': fgs,
        'formA': form
    }



    return render(request, 'preorderlevel.html', var)


@login_required(login_url='login')
def availableStock (request):
    return render(request, 'availbleStock.html')


@login_required(login_url='login')
def addlevel (request):

    formAdd = PreOrderLevelForm()

    if request.method == 'POST':
        form = PreOrderLevelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Added Successfully')
                return redirect('preorderlevel')
            except Exception as e:
                print(e)
                pass
        else:
            messages.success(request, 'Already Exist...  ')
            return redirect('preorderlevel')
    #aasign all objects
    array = preorder.objects.all()

    #aasign form
    var = {'preordelevelform': form}

    alldetails = {'formAdd': var, 'orderlevel':array}


    return render(request, 'preorderlevel.html', {'formAdd': formAdd})

@login_required(login_url='login')
def editlevel (request):

    if request.method == 'POST':
        levelId = request.POST.get('lid')

        if levelId is not None:

            try:
                level = preorder.objects.get(pk=levelId)
                form = PreOrderLevelForm(instance=level)

                return render(request, 'preorderlevel.html', {'pForm': form, 'PID': levelId})

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'editlevel.html')

#
# @login_required(login_url='login')
# def deletelevel(request):
#
#     if request.method == 'POST':
#         levelId = request.POST.get('lid')
#
#         if levelId is not None:
#             level = preorder.objects.get(pk=levelId)
#             lform = PreOrderLevelForm(request.POST, instance=level)
#
#             if lform.is_valid():
#                 lform.save()
#                 return redirect('viewpackets')
#
#             else:
#                 #invalid
#                 return render(request, 'preorderlevel.html', {'lform': lform, 'PID': levelId})
#
#         else:
#             pass
#
#     return render(request, 'preorderlevel.html')
#
# @login_required(login_url='login')
# def deletepackets(request):
#
#     levelId = request.POST.get('deleteid')
#
#     if request.method == 'POST' and levelId is not None:
#         level = preorder.objects.get(id=levelId)
#         level.delete()
#     return redirect('preorderlevel')
