from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.generic.edit import FormView


def index(request):
    return render(request, 'cafe/index.html')



