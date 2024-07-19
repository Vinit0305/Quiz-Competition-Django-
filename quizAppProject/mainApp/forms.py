from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

class RegisterUser(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username', 'email', 'password1')
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Surname'
                }),
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'password1': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                })
            
        }
