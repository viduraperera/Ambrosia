from django.shortcuts import render, redirect
from Ambrosia_Project.forms import RegistrationForm
from Ambrosia_Project.forms import LeafStockForm
from Ambrosia_Project.forms import PaymentForm
from Ambrosia_Project.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Ambrosia_Project.common_utills.filters import StockFilter, SupplierFilter


# Create your views here.

# Supplier Management --------------------------------------------------------------------------------------------------

# Navigate from Admin home to Registered Suppliers List
@login_required(login_url='login')
def to_reg_suppliers(request):
    suppliers = Registration.objects.all()

    sup_count = suppliers.count()

    supFilter = SupplierFilter(request.POST, queryset=suppliers)
    suppliers = supFilter.qs

    return render(request, 'SupplierManagement templates/AllRegisteredSuppliers.html', {'Sup': suppliers, 'supFilter': supFilter})


# Navigate from All Registered Suppliers List to Registration Form
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
    return render(request, 'SupplierManagement templates/SupRegistration.html', var)


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


    return render(request, 'AllRegisteredSuppliers.html')


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

                return render(request, 'SupplierManagement templates/ViewSupplierProfile.html', {'sFrom': form, 'SupId': supid, 'img': img})

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'SupplierManagement templates/AllRegisteredSuppliers.html')


# Navigate from Supplier Profile to Edit Supplier
# @login_required(login_url='login')
# def to_edit_profile(request):
#   return render(request, 'EditSupplier.html')


# Navigate from Registered Suppliers List to Stock Details
#Edited 2020-10-9 for add order by function
@login_required(login_url='login')
def to_stock_details(request):
    form = LeafStock.objects.all()

    order_count = form.count()

    myFilter = StockFilter(request.POST, queryset=form)
    form = myFilter.qs

    return render(request, 'SupplierManagement templates/StockDetails.html', {'form': form, 'myFilter': myFilter})


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

    return render(request, 'SupplierManagement templates/StockDetails.html')


# editLeafStock(Temporary)
@login_required(login_url='login')
def to_edit_stock_details(request):
    formid = request.POST.get('formid')

    form = LeafStock.objects.get(id=formid)

    return render(request, 'SupplierManagement templates/EditStockDetails.html', {'form': form})


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
                    #return render(request, 'AllRegisteredSuppliers.html', {'sFrom': form, 'SupId': sid, 'img': img})
                    return redirect('S_AllRegisteredSuppliers')

                else:
                    # invalid
                    return render(request, 'SupplierManagement templates/ViewSupplierProfile.html', {'sFrom': form, 'SupId': sid})
                    pass

            except Exception as e:
                print(e)

        else:
            pass

    return render(request, 'SupplierManagement templates/AllRegisteredSuppliers.html')


# editLeafStockSubmit(Temporary)
@login_required(login_url='login')
def updated_leaf_stock(request):
    formid = request.POST.get('formid')

    if request.method == 'POST' and formid is not None:
        form = LeafStock.objects.get(id=formid)
        form.save()

        return render(request, 'SupplierManagement templates/StockDetails.html', {'form': form})


# edit Supplier Details
@login_required(login_url='login')
def update_sup_details(request):
    supid = request.POST.get('supid')

    if request.method == 'POST' and supid is not None:
        sup = LeafStock.objects.get(id=supid)
        sup.save()

    return render(request, 'SupplierManagement templates/AllRegisteredSuppliers.html')


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
    return render(request, 'SupplierManagement templates/LeafStock.html', var)


# Navigate from Registered Suppliers List to Payments Details
@login_required(login_url='login')
def to_sup_payments(request):
    form2 = PaymentForm()

    if request.method == "POST":

        form2 = PaymentForm(request.POST)

        if form2.is_valid():
            try:
                form2.save()
                return redirect('S_PaymentDetails')

            except:
                pass

    var = {'form': form2}
    return render(request, 'SupplierManagement templates/SupPayments.html', var)


# Navigate from Payments to Payment Details Table
#Edited 2020-10-10 for add order by function for payments
@login_required(login_url='login')
def to_pay_details(request):
    form = Payment.objects.all()

    order_count = form.count()

    payFilter = StockFilter(request.POST, queryset=form)
    form = payFilter.qs

    return render(request, 'SupplierManagement templates/PaymentDetails.html', {'form': form, 'payFilter': payFilter})


# Navigate from Payments to Payment Details Table
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

    return render(request, 'SupplierManagement templates/AllRegisteredSuppliers.html')
