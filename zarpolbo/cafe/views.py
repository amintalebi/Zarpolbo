from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.generic.edit import FormView

from cafe.models import Cafe


def index(request):
    try:
        cafes_list = Cafe.objects.all()
    except:
        raise Http404("No Cafe")
    context = {
        'cafes_list' : cafes_list
    }
    return render(request, 'cafe/index.html', context)



