# coding: utf-8
from django import forms
from registration.forms import RegistrationFormUniqueEmail, RegistrationForm
from django.contrib.auth.forms import UserCreationForm 

from models import User

class UserForm(RegistrationFormUniqueEmail):
    
    class  Meta(RegistrationForm.Meta):
        model = User
        
        fields = [
            User.USERNAME_FIELD,
            'first_name',
            'email',
            'password1',
            'password2',
        ]                     

