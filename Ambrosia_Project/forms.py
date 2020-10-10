from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Ambrosia_Project.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']


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

