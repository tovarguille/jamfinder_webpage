from django import forms
from .models import Local
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['name', 'type_of_studio', 'address', 'opening_hours', 'price', 'services', 'phone_number']
