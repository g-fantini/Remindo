from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import re

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2" ]
                  
class ProfileRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['phone']
    
    def clean_phone(self, *args, **kwargs):
        phone = self.cleaned_data.get("phone")
        
        #define basic regex for UK phone numbers
        regex= "0\d{10}$" 
        
        #validate the phone number submitted
        if re.search(regex, phone):
            return phone
        else:
           raise forms.ValidationError("Invalid phone number")
            