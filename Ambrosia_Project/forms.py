from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Ambrosia_Project.models import categoryProduct, packetType, teaCategory, preorder, addPackets


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']


class PacketTypeForm(forms.ModelForm):
    class Meta:
        model = packetType
        fields = '__all__'


class TeaCategoryForm(forms.ModelForm):
     class Meta:
          model = teaCategory
          fields = '__all__'


class AddTeaPacketsForm(forms.ModelForm):
    class Meta:
        model = addPackets
        fields = ['date', 'category', 'weight', 'noOfPackets']


class PreOrderLevelForm(forms.ModelForm):
    class Meta:
        model = preorder
        fields = '__all__'
