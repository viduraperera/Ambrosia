from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ambrosia_Project.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Ambrosia_Project.models import *
from Ambrosia_Project.forms import *


# Create your views here.


@login_required(login_url='login')
def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'User Account ' + user + ' Created Successfully.')
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
def teashopHomepage(request):
    return render(request, 'teashophome.html')


@login_required(login_url='login')
def EmployeeHome(request):
    return render(request, 'attendance_date.html')


@login_required(login_url='login')
def attendance_management(request):

    if request.method == 'POST':

        dateView = request.POST.get('date')

        attend = attendance.objects.filter(date=dateView).select_related('empID')

        return render(request, 'attendance_management.html', {'attendance': attend, 'date': dateView })

    return redirect('attendance_date')


@login_required(login_url='login')
def updatemark_attendance(request):

    if request.method == 'POST':

       date = request.POST.get('date')
       empId = request.POST.get('workersid')
       type = request.POST.get('dayType')

       attend = attendance.objects.get(empID=empId, date=date)

       try:

            if type is not None:

                if type == 'halfDay':
                    type = 'HalfDay'

                else:
                    type = 'FullDay'

                print(type)

                #present
                attend.attendaceStatus = "Present"
                attend.daytype = type
                attend.save()

            else:
                 # absent
                 attend.attendaceStatus = "Absent"
                 attend.daytype = None
                 attend.save()


            attend = attendance.objects.filter(date=date).select_related('empID')

            return render(request, 'attendance_management.html', {'attendance': attend, 'date': date})


       except Exception as e:
        print(e)

    return redirect('attendance_date')



@login_required(login_url='login')
def staff_management(request):

    arr = Employee.objects.filter(empGroup='staff')

    return render(request, 'staff_management.html', {'Employee': arr})


@login_required(login_url='login')
def factoryworkers_management(request):

    arr = Employee.objects.filter(empGroup='factory_Worker')

    return render(request, 'factoryworkers_management.html', {'Employee': arr})


@login_required(login_url='login')
def showAttendance(request):
    arr = Employee.objects.filter(empGroup='factory_Worker')
    workingDays = attendance.workingDays

    return render(request, 'attendance_management.html', {'Employee': arr}, workingDays)


@login_required(login_url='login')
def selectAttendence(request):

    return render(request, 'attendance_date.html')


@login_required(login_url='login')
def viewMarkAttendance(request):

    if request.method == 'POST':

        date = request.POST.get('currDate')

        attend = attendance.objects.filter(date=date).filter(attendaceStatus__in=['Present','Absent']).values('empID')
        arr = Employee.objects.exclude(id__in=attend).filter(empGroup='factory_Worker')

        return render(request, 'mark_attendance.html', {'Employee': arr, 'date': date })

    return redirect('attendance_date')



@login_required(login_url='login')
def markAttendance(request):

    if request.method == 'POST':
        empID = request.POST.get('workersid')
        dayType = request.POST.get('dayType')
        date = request.POST.get('date')
        emp = Employee.objects.get(pk=empID)
        try:

            if dayType is not None:

                dayt = 'FullDay'

                if dayType == 'halfDay':
                    dayt = 'HalfDay'

                #present
                attend = attendance()
                attend.date = date
                attend.empID = emp
                attend.attendaceStatus = "Present"
                attend.daytype = dayt
                attend.save()

            else:
                 # absent
                 attend = attendance()
                 attend.date = date
                 attend.empID = emp
                 attend.attendaceStatus = "Absent"
                 attend.save()

            atten = attendance.objects.filter(date=date).filter(attendaceStatus__in=['Present', 'Absent'])\
                .values('empID')
            arrEmp = Employee.objects.exclude(id__in=atten).filter(empGroup='factory_Worker')
            messages.success(request, 'Successfully Added Details')
            return render(request, 'mark_attendance.html', {'Employee': arrEmp, 'date': date})

        except Exception as e:
            print(e)

    return redirect('attendance_date')


@login_required(login_url='login')
def edit_employee(request):

    if request.method == "POST":
        eid = request.POST.get('workersid')

        if eid is not None:

            try:
                employee = Employee.objects.get(pk=eid)
                eform = RegisterEmployee(instance=employee)
                return render(request, 'edit_employee.html' , {'form': eform , 'EmpId' : eid } )

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'edit_employee.html')


@login_required(login_url='login')
def update_employee(request):

    if request.method == 'POST':
        eid = request.POST.get('empId')

        if eid is not None:
            employee = Employee.objects.get(pk=eid)
            form = RegisterEmployee(request.POST, instance=employee)

            if form.is_valid():
                form.save()
                try:

                    if (form.cleaned_data.get('empGroup') == 'factory_Worker'):
                        messages.success(request, 'update successful')
                        return redirect('factoryworkers_management')

                    else:
                        messages.success(request, 'update successful')
                        return redirect('staff_management')

                except Exception as e:
                    print(e)
                    messages.success(request, 'Exception:' + e)

            else:
                messages.error(request, "Can't Update Details.")
                return redirect('edit_employee')

        else:
            messages.error(request, "Can't Update Details.")
            return redirect('edit_employee')


@login_required(login_url='login')
def view_employee(request):

    id = request.POST.get("workersid")

    employee = Employee.objects.get(pk=id)

    return render(request, 'view_employee.html', {'employee':employee} )


@login_required(login_url='login')
def employee_registration(request):
    form = RegisterEmployee()

    if request.method == 'POST':
        form = RegisterEmployee(request.POST)
        print(form.errors)
        if form.is_valid():
            try:
                form.save()
                if (form.cleaned_data.get('empGroup') == 'factory_Worker'):
                    messages.success(request,'Factory worker added successfully')
                    return redirect('factoryworkers_management')
                else:
                    messages.success(request,'Staff added successfully')
                    return redirect('staff_management')

            except Exception as e:
                print(e)
                messages.success(request, 'Exception:' +e)

        else:
            print(form.errors)
            messages.error(request, 'Invalid Details')
            pass

    var = {'form': form}
    return render(request, 'employee_registration.html', var)


@login_required(login_url='login')
def deleteEmployee(request):
    workersid = request.POST.get('workersid')
    print(workersid)

    if request.method == 'POST' and workersid is not None:
        worker = Employee.objects.get(id=workersid)

        workerType = worker.empGroup

        worker.delete()

        if workerType == 'staff':
            messages.success(request, 'Employee Deleted successfully')
            return redirect('staff_management')

        else:
            messages.success(request, 'Employee Deleted successfully')
            return redirect('factoryworkers_management')



# Navigate from Admin home to Registered Suppliers List
@login_required(login_url='login')
def to_reg_suppliers(request):
    return render(request, 'AllRegisteredSuppliers.html')


@login_required(login_url='login')
def NavigateToInventory(request):
    return render(request, 'add_inventory.html')



@login_required(login_url='login')
def NavigateToProduction(request):
    return render(request, 'Add_daily_product.html')