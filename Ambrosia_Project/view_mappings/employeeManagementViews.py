from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Ambrosia_Project.forms import *


# Create your views here.

#-----Employee Management Malka--------------------------------------------------------------------------
@login_required(login_url='login')
def EmployeeHome(request):
    return render(request, 'EmployeeManagement_templates/attendance_date.html')


@login_required(login_url='login')
def attendance_management(request):
    return render(request, 'EmployeeManagement_templates/attendance_management.html')


@login_required(login_url='login')
def staff_management(request):

    arr = Employee.objects.filter(empGroup='staff')

    return render(request, 'EmployeeManagement_templates/staff_management.html', {'Employee': arr})


@login_required(login_url='login')
def factoryworkers_management(request):

    arr = Employee.objects.filter(empGroup='factory_Worker')

    return render(request, 'EmployeeManagement_templates/factoryworkers_management.html', {'Employee': arr})


@login_required(login_url='login')
def showAttendance(request):
    arr = Employee.objects.filter(empGroup='factory_Worker')
    workingDays = attendance.workingDays

    return render(request, 'EmployeeManagement_templates/attendance_management.html', {'Employee': arr}, workingDays)


@login_required(login_url='login')
def selectAttendence(request):

    return render(request, 'EmployeeManagement_templates/attendance_date.html')


@login_required(login_url='login')
def viewMarkAttendance(request):

    if request.method == 'POST':

        date = request.POST.get('currDate')

        arr = Employee.objects.filter(empGroup='factory_Worker')
        attend = attendance.objects.all()

        return render(request, 'EmployeeManagement_templates/mark_attendance.html', {'Employee': arr, 'date': date, 'attend': attend})

    return redirect('attendance_date')



@login_required(login_url='login')
def markAttendance(request):

    if request.method == 'POST':
        empID = request.POST.get('workersid')
        dayType = request.POST.get('dayType')
        date = request.POST.get('date')

        arrEmp = Employee.objects.filter(empGroup='factory_Worker')

        try:

            if dayType is not None:

                dayt = 'FullDay'

                if dayType == 'halfDay':
                    dayt = 'HalfDay'

                #present
                attend = attendance()
                attend.date = date
                attend.empID = empID
                attend.attendaceStatus = "Present"
                attend.daytype = dayt
                attend.save()

            else:
                 # absent
                 attend = attendance()
                 attend.date = date
                 attend.empID = empID
                 attend.attendaceStatus = "Absent"
                 attend.save()

            messages.success(request, 'Successfully Added Details')
            return render(request, 'EmployeeManagement_templates/mark_attendance.html', {'Employee': arrEmp, 'date': date})

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
                return render(request, 'EmployeeManagement_templates/edit_employee.html', {'form': eform , 'EmpId' : eid})

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'EmployeeManagement_templates/edit_employee.html')


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

    return render(request, 'EmployeeManagement_templates/view_employee.html', {'employee':employee})


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
    return render(request, 'EmployeeManagement_templates/employee_registration.html', var)


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

