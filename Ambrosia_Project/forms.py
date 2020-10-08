from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Ambrosia_Project.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']


class AddVehicle(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class AddDriver(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleRecordsForm(forms.ModelForm):
    class Meta:
        model = Driving_Records
        fields = '__all__'


# class OilForm(forms.ModelForm):
#     class Meta:
#         model = Oil
#         fields = '__all__'
#
#
# class Oil_StockForm(forms.ModelForm):
#     class Meta:
#         model = Oil_Stock
#         fields = '__all__'



class RepairForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

