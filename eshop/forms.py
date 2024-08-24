from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control mt-2','autofocus':'True','autocomplete':'current-password'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control mt-2','autofocus':'True','autocomplete':'current-password'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control mt-2','autofocus':'True','autocomplete':'current-password'}))

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


class MysetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control','autofocus':'True','autocomplete':'current-password'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','autofocus':'True','autocomplete':'current-password'}))


class CustomerAddressForm(forms.ModelForm):
    address_choice = [("Home","Home"),("Work","Work")]
    state_choice = [
    ('Andhra Pradesh','Andhra pradesh'),
    ('Karnataga','karnataga'),
    ('Tamilnadu','Tamilnadu'),
    ('Kerala','Kerala')
    ]
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    locality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'locality'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'house'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}))
    landmark = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'landmark'}))
    state = forms.CharField(widget=forms.Select(choices=state_choice,attrs={'class':'form-select','placeholder':'state'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'mobile'}))
    zipcode = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'pincode'}))
    address_type = forms.ChoiceField(choices=address_choice,widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    class Meta:
        model = Customer
        fields = ['name','locality','city','address','landmark','mobile','state','zipcode','address_type']
        
