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
        fields ='__all__'
