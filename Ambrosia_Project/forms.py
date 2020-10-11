from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Ambrosia_Project.models import *
from django.core.exceptions import ValidationError


#----User---------------------------------------------------------------------

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'is_superuser']


#----leaf inventory & daily Production - Ravija------------------------------------------------------------------------

class AddInventoryForm(forms.ModelForm):
    class Meta:
        model = LeafInventory
        fields = '__all__'


class AddSubProductForm(forms.ModelForm):
    class Meta:
        model = Final_product_sub
        fields = '__all__'


class AddMainProductForm(forms.ModelForm):
    class Meta:
        model = Final_product_Main
        fields = '__all__'


class AddTeaGradeform(forms.ModelForm):
    class Meta:
        model = TeaGrades
        fields = '__all__'


#final production management - Auction Stock - Sandun ---------------------------------------------------------------

class AddBrokerForm(forms.ModelForm):
    class Meta:
        model = Broker
        fields = '__all__'


class AddBuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'


class AddSubAuctionStockForm(forms.ModelForm):

    class Meta:
        model = Auction_SubStock
        fields = '__all__'

    def clean(self):
        netW = self.cleaned_data['net_weight']
        totW = self.cleaned_data['total_weight']

        if netW > totW:
            raise ValidationError('Total Weight Must grate than Net Weight')


class AddMainAuctionStockForm(forms.ModelForm):

    class Meta:
        model = Auction_MainStock
        fields = '__all__'


class AddAuctionSoldStockForm(forms.ModelForm):

    class Meta:
        model = Auction_SoldStocks
        fields = '__all__'


class AddAuctionNotSoldStockForm(forms.ModelForm):

    class Meta:
        model = Auction_NotSoldStocks
        fields = '__all__'

class AuctionNotSoldStockLogForm(forms.ModelForm):
    class Meta:
        model = Auction_NotSoldStocksLog
        fields = '__all__'


#Tea shop inventory Nethmi------------------------------------------------------------
class AddTeaPacketsForm(forms.ModelForm):
    class Meta:
        model = AddPackets
        fields = '__all__'


class AddcategoryProductForm(forms.ModelForm):
    class Meta:
        model = CategoryProduct
        fields = '__all__'


#Tea shop Sales Onella-------------------------------------------------------
class TransactionForm(forms.ModelForm):
    class Mate:
        module = Transactions
        fields = '__all__'


class billItemsForm(forms.ModelForm):
    class Meta:
        model = BillItems
        fields = '__all__'


class priceTableForm(forms.ModelForm):
    class Meta:
        model = Price_Table
        fields ='__all__'


#Transportation Nethmi W--------------------

class AddVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleRecordsForm(forms.ModelForm):
    class Meta:
        model = Driving_Records
        fields = '__all__'


class RepairForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


# Supplier Management------------------------------------------------------------------------------------------------

# Supplier Management Registration
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"


class LeafStockForm(forms.ModelForm):
    class Meta:
        model = LeafStock
        fields = "__all__"

#-------Salary Management-------------------------------------------------------
class FundFrom(forms.ModelForm):
    class Meta:
        model = Funds
        fields = '__all__'


class AllowanceForm(forms.ModelForm):
    class Meta:
        model = Allowance
        fields = '__all__'


class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'


#-----Employee Management Malka--------------------------------------------------------------------------
class RegisterEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class MarkAttendance(forms.ModelForm):
    class Meta:
        model = attendance
        fields = '__all__'
