from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm


