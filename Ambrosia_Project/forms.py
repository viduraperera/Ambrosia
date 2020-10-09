from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Ambrosia_Project.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']


class RegisterEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class MarkAttendance(forms.ModelForm):
    class Meta:
        model = attendance
        fields = '__all__'
