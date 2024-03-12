from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model=User
        # fields="__all__"
        fields=['username','first_name','last_name','email']
        

class changeUserdata(UserChangeForm):
    password=None # hide this 
    class Meta:
        model=User
        # fields='__all__'
        fields=['username','first_name','last_name','email']
