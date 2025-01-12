from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Email kiriting")

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone_number','password1', 'password2']


# class RegisterForm(UserCreationForm):
#     password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
#         attrs={'class':'form-control','type':'password','placeholder':'Confirm password'}
#     ),)
#     password2 = forms.CharField(label="Password", widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm password'}
#     ),)
#     class Meta:
#         model = UserProfile
#         fields = ['username','email','phone_number','password1','password2']

#         widgets = {
#             'username':forms.TextInput(attrs={'name':'username', 'class':'form-control'}),
#             'email':forms.EmailInput(attrs={'name':'email','class':'form-control','placeholder':'Enter your email'}),
#             'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter phone number'}),
#         }

