from django import forms
from .models import Ad
from .models import Director
from django.contrib.auth.models import User, auth


class AdForm(forms.Form):
    name = forms.CharField(max_length=100)
    details = forms.CharField(max_length=500)
    price = forms.IntegerField()
    director = forms.ModelChoiceField(queryset=Director.objects.all())
    user = forms.ModelChoiceField(queryset=User.objects.all())


class DirectorForm(forms.Form):
     name = forms.CharField(max_length=100)
     details = forms.CharField(max_length=500)
     age = forms.IntegerField()
     experience = forms.IntegerField()
     isCreep = forms.BooleanField()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
 