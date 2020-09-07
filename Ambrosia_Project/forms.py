from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Ambrosia_Project.models import Funds


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']


class FundFrom(forms.ModelForm):
    class Meta:
        model = Funds
        fields = '__all__'
        # field_classes = {'emp_epf': forms.CharField}
