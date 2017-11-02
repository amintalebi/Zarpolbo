# coding=utf-8
from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from account.models import UserInfo


class RegisterForm(UserCreationForm):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')


class UserInfoForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = UserInfo
        fields = ('profile_picture',)

