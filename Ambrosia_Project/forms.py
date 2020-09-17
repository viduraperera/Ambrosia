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


#final production management - Auction Stock - Sandun

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

class AddMainAuctionStockForm(forms.ModelForm):

    class Meta:
        model = Auction_MainStock
        fields = '__all__'