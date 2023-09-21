from django import forms
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"placeholder": "First name", "class": "form-control"}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"placeholder": "Last name", "class": "form-control"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}))
    username = forms.CharField(min_length=8, widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}))
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]