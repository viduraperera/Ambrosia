from django.shortcuts import render, redirect

from Ambrosia_Project.forms import CreateUserForm
from Ambrosia_Project.forms import RegistrationForm
from Ambrosia_Project.forms import LeafStockForm
from Ambrosia_Project.forms import PaymentForm
from Ambrosia_Project.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .filters import StockFilter, SupplierFilter, PaymentFilter

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
        pword = request.POST.get('pwd')

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


# Navigate from Admin home to Registered Suppliers List
#also contains views file to filter search
@login_required(login_url='login')
def to_reg_suppliers(request):
    suppliers = Registration.objects.all()

    sup_count = suppliers.count()

    supFilter = SupplierFilter(request.POST, queryset=suppliers)
    suppliers = supFilter.qs

    return render(request, 'AllRegisteredSuppliers.html', {'Sup': suppliers, 'supFilter': supFilter})


# Navigate from All Registered Suppliers List to Registration Form
#take inputs
@login_required(login_url='login')
def to_sup_registration(request):
    sup = RegistrationForm()
    if request.method == "POST":
        sup = RegistrationForm(request.POST, request.FILES)
        if sup.is_valid():
            try:
                sup.save()
                return redirect('S_AllRegisteredSuppliers')
            except:
                pass
    else:
        # sup = RegistrationForm()
        pass

    var = {'sup': sup}
    return render(request, 'SupRegistration.html', var)


# Registration with validations
@login_required(login_url='login')
def add_supplier(request):
    supnic = request.POST.get('supnic')

    if request.method == 'POST' and supnic is not None:
        sup = Registration.objects.get(id=supnic)

        if sup.is_valid():
            try:
                sup.save()
                messages.success(request, "Supplier Added Successfully!")  # validations
                return redirect('S_AllRegisteredSuppliers')

            except Exception as e:
                # pass
                print(e)
                messages.success(request, "Exception : " + e)
                return redirect('S_SupRegistration')

        else:
            # method invalid
            print(sup.errors)
            messages.success(request, "Added Failed! Check inputs and try again!")
            pass

    return render(request, 'S_AllRegisteredSuppliers.html')


# Navigate from Registered Suppliers List to View Supplier Profile
@login_required(login_url='login')
def to_sup_profile(request):
    if request.method == 'POST':
        supid = request.POST.get('supid')

        if supid is not None:

            try:
                supplier = Registration.objects.get(pk=supid)

                form = RegistrationForm(instance=supplier)

                img = form.instance

                return render(request, 'ViewSupplierProfile.html', {'sFrom': form, 'SupId': supid, 'img': img})

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'AllRegisteredSuppliers.html')


# Navigate from Registered Suppliers List to Stock Details
# Edited 2020-10-9 for add order by function
@login_required(login_url='login')
def to_stock_details(request):
    form = LeafStock.objects.all()

    order_count = form.count()

    myFilter = StockFilter(request.POST, queryset=form)
    form = myFilter.qs

    return render(request, 'StockDetails.html', {'form': form, 'myFilter': myFilter})


# delete Stock Details
@login_required(login_url='login')
def leaf_stock_delete(request):
    formid = request.POST.get('formid')

    if request.method == 'POST' and formid is not None:
        form = LeafStock.objects.get(id=formid)
        form.delete()

    return redirect('S_StockDetails')


# add Stock Details
@login_required(login_url='login')
def leaf_stock_add(request):
    formtime = request.POST.get('formtime')

    if request.method == 'POST' and formtime is not None:
        form = LeafStock.objects.get(id=formtime)
        form.save()

    return render(request, 'StockDetails.html')


# edit Supplier
@login_required(login_url='login')
def to_edit_supplier(request):
    if request.method == 'POST':
        sid = request.POST.get('SID')
        # supplier = Registration.objects.all()

        if sid is not None:

            try:
                supplier = Registration.objects.get(pk=sid)
                form = RegistrationForm(request.POST, instance=supplier)

                if form.is_valid():
                    form.save()
                    img = form.instance
                    # return render(request, 'AllRegisteredSuppliers.html', {'sFrom': form, 'SupId': sid, 'img': img})
                    return redirect('S_AllRegisteredSuppliers')

                else:
                    # invalid
                    return render(request, 'ViewSupplierProfile.html', {'sFrom': form, 'SupId': sid})
                    pass

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'AllRegisteredSuppliers.html')


# Navigate from Stock Details to Add Leaf Stock
@login_required(login_url='login')
def to_leaf_stock(request):
    form1 = LeafStockForm()
    if request.method == "POST":
        form1 = LeafStockForm(request.POST)
        if form1.is_valid():
            try:
                form1.save()
                return redirect('S_StockDetails')
            except:
                pass

    var = {'form': form1}
    return render(request, 'LeafStock.html', var)


# Navigate from Registered Suppliers List to Payments Details
@login_required(login_url='login')
def to_sup_payments(request):
    form = PaymentForm()

    if request.method == "POST":

        form = PaymentForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('S_PaymentDetails')

            except:
                pass
    else:
        pass

    var = {'form': form}
    return render(request, 'SupPayments.html', var)


# Navigate from Payments to Payment Details Table
# Edited 2020-10-10 for add order by function for payments
@login_required(login_url='login')
def to_pay_details(request):
    form = Payment.objects.all()

    pay_count = form.count()

    payFilter = PaymentFilter(request.POST, queryset=form)
    form = payFilter.qs

    return render(request, 'PaymentDetails.html', {'form': form, 'payFilter': payFilter})
    # return redirect('S_PaymentDetails')


# Calculating Payment
@login_required(login_url='login')
def calc_payment(request):
    if request.method == 'POST':

        form = PaymentForm(request.POST)

        if form.is_valid():
            try:
                # calculation
                totalW = form.cleaned_data['tot_weight']
                kiloPrice = form.cleaned_data['per_kilo_price']
                addition = form.cleaned_data['additions']
                advances = form.cleaned_data['advances']
                transport_costs = form.cleaned_data['transport_costs']
                other_costs = form.cleaned_data['other_costs']

                finalPayment = (totalW * kiloPrice) + addition - advances - transport_costs - other_costs

                payObj = form.save(commit=False)
                payObj.payment = finalPayment
                payObj.save()

                messages.success(request, "Calculated Successfully!")

                return redirect('S_PaymentDetails')

            except Exception as e:
                print(e)
                messages.success(request, "Exception : " + e)
                return redirect('S_SupPayments')
        else:
            print(form.errors)
            messages.success(request, "Added Failed! Check input values and try again!")
            pass

    return render(request, 'PaymentDetails.html')


# delete Payment Table Details
@login_required(login_url='login')
def payment_delete(request):
    formid = request.POST.get('formid')

    if request.method == 'POST' and formid is not None:
        form = Payment.objects.get(id=formid)
        form.delete()

    return redirect('S_PaymentDetails')


@login_required(login_url='login')
def delete_supplier(request):
    if request.method == 'POST':
        supID = request.POST.get('supid')

        if supID is not None:
            try:
                supplier = Registration.objects.get(pk=supID)
                supplier.delete()
                return redirect('S_AllRegisteredSuppliers')

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'AllRegisteredSuppliers.html')