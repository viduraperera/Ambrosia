from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Ambrosia_Project.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']


class FundFrom(forms.ModelForm):
    class Meta:
        model = Funds
        fields = '__all__'


class AllowanceForm(forms.ModelForm):
    class Meta:
        model = Allowance
        fields = '__all__'


class AccumulateForm(forms.ModelForm):
    class Meta:
        module = Accumulate
        fields = '__all__'


class PacketStockForm(forms.ModelForm):
    class Meta:
        module = Packet_stock
        fields = '__all__'


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












