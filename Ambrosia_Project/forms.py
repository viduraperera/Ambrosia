from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Ambrosia_Project.models import Payment, Registration
from Ambrosia_Project.models import LeafStock


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']


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








