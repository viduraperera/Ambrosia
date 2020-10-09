from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from Ambrosia_Project.forms import *
from Ambrosia_Project.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
from Ambrosia_Project.utils import render_to_pdf


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





#transport management
#add vehicle
@login_required(login_url='login')
def Vehicle_Records(request):

    form = AddVehicle()

    if request.method == 'POST':

        form = AddVehicle(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('addVehicle')
            except Exception as e:
                print(e)
                pass

    #assign all vehicle objects
    array = Vehicle.objects.all()

    #assign form
    var = {'vehicleForm': form}


    alldetails = {'Vform':var , 'AllVehicle':array }

    return render(request, 'AddVehicle.html', alldetails)

#delete vehicle
@login_required(login_url='login')
def deleteVehicleRecord(request):

    id = request.POST.get('id')

    if request.method == 'POST' and id != None:
        vehicle = Vehicle.objects.get(id=id)
        vehicle.delete()

    return redirect('addVehicle ')



#add driver

@login_required(login_url='login')
def driver_records(request):

    form = AddDriver()

    if request.method == 'POST':

        form = AddDriver(request.POST)

        if form.is_valid():
            try:
                # epfno = form.cleaned_data("epfNo")
                # result = checkEpNo(epfno)

                form.save()
                messages.success(request, 'Successfully added driver details')
                return redirect('Transport')

            except Exception as e:
                print(e)
                messages.success(request, 'Exception:'+ e)

        else:
            print(form.errors)
            messages.success(request, 'Invalid Details')


    #assign all vehicle objects
    array = Driver.objects.all()

    #assign form
    var = {'driverForm': form}


    allDdetails = {'VDform':var , 'AllDriver':array }

    return render(request, 'AddDriver.html', allDdetails)

#delete driver
@login_required(login_url='login')
def deleteDriverRecord(request):

    id = request.POST.get('id')

    if request.method == 'POST' and id != None:
        driver = Driver.objects.get(id=id)
        driver.delete()

    return redirect('Transport')

#display driver
@login_required(login_url='login')
def DisplayDriverRecord(request):

    if request.method == 'POST':
        id = request.POST.get('Did')

        if id is not None:
            try:
                driver = Driver.objects.get(pk=id)
                driverForm = AddDriver(instance=driver)
                return render(request, 'UpdateDriver.html', {'Dform': driverForm, 'DId':id } )

            except Exception as e:
                print(e)

        else:
            pass

    else:
        pass

    return redirect('Transport')

#update driver records
@login_required(login_url='login')
def UpdateDriverRecord(request):

    if request.method == 'POST':
        dID = request.POST.get('DID')

        if dID is not None:

            try:
                driver = Driver.objects.get(pk=dID)
                form_update = AddDriver(request.POST, instance=driver)

                if form_update.is_valid():
                    form_update.save()
                    return redirect('AddDriver')

                else:
                    #invalid
                    pass

            except Exception as e:
                print(e)

        else:
            #id not found
            pass

    return redirect('Transport')



#add vehicle driving records
@login_required(login_url='login')
def DrivingRecords(request):

    form = VehicleRecordsForm()
    diff = 0

    if request.method == 'POST':

        form = VehicleRecordsForm(request.POST)

        if form.is_valid():
            try:
                start = form.cleaned_data['Start_Reading']
                end = form.cleaned_data['End_Reading']
                diff = int(end) - int(start)

                if diff > 0:

                    form_mread = form.save(commit=False)
                    form_mread.Meter_Difference = diff

                    form.save()
                    messages.success(request, 'Successfully added driver details')
                    return redirect('RecordTable')

                else:
                    messages.error(request, 'End reading Number Error')

            except Exception as e:
                print(e)
                messages.error(request, 'Exception:' + e)

        else:
            print(form.errors)
            messages.error(request, 'Invalid Details')

    # assign form
    var = {'RecordForm': form}

    return render(request, 'VehicleRecords.html', var)

#show driving records
@login_required(login_url='login')
def ShowDrivingRecords(request):

    records = Driving_Records.objects.all()

    return render(request, 'VehicleRecordsTable.html', {'records': records})



#delete vehicle driving records
@login_required(login_url='login')
def deleteRecords(request):

    id = request.POST.get('id')

    if request.method == 'POST' and id != None:
        record = Driving_Records.objects.get(id=id)
        record.delete()

    return redirect('RecordTable')



#
# #add oil
# @login_required(login_url='login')
# def AddFuelLog(request):
#
#     form = OilForm()
#
#     if request.method == 'POST':
#
#         form = OilForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('ViewOilTable')
#
#             except Exception as e:
#                 print(e)
#                 pass
#
#
#     #assign form
#     var = {'OilForm': form}
#
#     return render(request, 'FuelLog.html', var)
#
# #view oil table
# @login_required(login_url='login')
# def ShowOil(request):
#
#     oil = Oil.objects.all()
#
#     return render(request, 'ViewOilTable.html', {'oil': oil})
#
#
#
# #delete oil
# @login_required(login_url='login')
# def deleteOilRecords(request):
#
#     id = request.POST.get('id')
#
#     if request.method == 'POST' and id != None:
#         oil = Oil.objects.get(id=id)
#         oil.delete()
#
#     return redirect('ViewOilTable')
#
#
# #add oil stock
# @login_required(login_url='login')
# def AddOil_Stock(request):
#
#     form = Oil_StockForm()
#
#     if request.method == 'POST':
#
#         form = Oil_StockForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('Oil_Stock')
#             except Exception as e:
#                 print(e)
#                 pass
#
#     #assign all oil stock objects
#     array = Oil_Stock.objects.all()
#
#     #assign form
#     var = {'oil_stockForm': form}
#
#
#     alldetails = {'OSform':var , 'AllStock':array }
#
#     return render(request, 'Oil_Stock.html', alldetails)
#
# #delete oil stock
# @login_required(login_url='login')
# def deleteOil_StockRecords(request):
#
#     id = request.POST.get('id')
#
#     if request.method == 'POST' and id != None:
#         oil_stock = Oil_Stock.objects.get(id=id)
#         oil_stock.delete()
#
#     return redirect('Oil_Stock')


#add vehicle repairs
@login_required(login_url='login')
def AddVehicleRepairs(request):

    form = RepairForm()

    if request.method == 'POST':

        form = RepairForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('RepairTable')

            except Exception as e:
                print(e)

                pass


    #assign form
    var = {'repairForm': form}

    return render(request, 'VehicleRepairs.html', var)


@login_required(login_url='login')
def ShowVehicleRepairs(request):

    repairs = Services.objects.all()

    return render(request, 'RepairTable.html', {'repairs': repairs})

#display repairs
@login_required(login_url='login')
def DisplayUpdateRepairs(request):

    if request.method == 'POST':

        id = request.POST.get('ReId')

        if id is not None:
            try:
                repair = Services.objects.get(pk=id)
                rForm = RepairForm(instance=repair)
                return render(request, 'EditRepairTable.html', {'REform': rForm, 'ReId':id } )

            except Exception as e:
                print(e)

        else:
            pass

    else:
        pass

    return redirect('RepairTable')



#update vehicle repairs
@login_required(login_url='login')
def UpdateVehicleRepairs(request):


    if request.method == 'POST':
        id = request.POST.get('repairID')

        if id is not None:

            try:
                repair = Services.objects.get(pk=id)
                form_update = RepairForm(request.POST, instance=repair)

                if form_update.is_valid():
                    form_update.save()

                else:
                    #invalid
                    pass

            except Exception as e:
                print(e)

        else:
            #id not found
            pass

    return redirect('RepairTable')


#delete repair details
@login_required(login_url='login')
def delete_RepairRecords(request):

    id = request.POST.get('id')

    if request.method == 'POST' and id != None:
        repair = Services.objects.get(id=id)
        repair.delete()

    return redirect('RepairTable')


#reports

@login_required(login_url='login')
def Reports(request):

    return render(request,'transportation_Reports.html')

#generate vehicle reports
class GenerateVehicle_RecordsPdf(View):
    def get(self, request, *args, **kwargs):

        vehicleNoInput = request.GET.get('vehicleno')
        month = request.GET.get('month')
        # date = request.GET.get('date')
        year = request.GET.get('year')
        vehicleNo = 0

        if len(month)== 2 and len(year)== 4:

            vehicle = Vehicle.objects.filter(VehicleNo=vehicleNoInput).first()

            if vehicle is not None:
                vehicleNo = vehicle.id

            records = Driving_Records.objects.filter(Date__month=month, Date__year=year , VehicleNo=vehicleNo)

            if len(records) > 0:

                total = 0

                for rec in records:
                    total = total + rec.Meter_Difference

                data = {
                    'Vrecords': records,
                    'year':year,
                    'month':month,
                    'total': total,
                    }

                pdf = render_to_pdf('Vehicle_Reports.html', data)
                return HttpResponse(pdf, content_type='application/pdf')

            else:
                messages.error(request, 'No Data Found')
                return redirect('Reports')

        else:
            messages.error(request, 'Invalid Inputs')
            return redirect('Reports')
