from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Ambrosia_Project.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']


class AddTeaPacketsForm(forms.ModelForm):
    class Meta:
        model = AddPackets
        fields = '__all__'


class AddcategoryProductForm(forms.ModelForm):
    class Meta:
        model = CategoryProduct
        fields = '__all__'
