from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from account.forms import RegisterForm


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = '/account/login/'

    def form_valid(self, form):
        result = super(RegisterView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        if User.objects.filter(username=username).count() == 0:
            User.objects.create_user(username=username, email=email, password=raw_password, first_name=name)

        return result


