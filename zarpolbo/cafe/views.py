import json

from django.core import serializers
from django.http import Http404
from django.http.response import HttpResponse
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
        'cafes_list': cafes_list
    }
    return render(request, 'cafe/index.html', context)


def search(request):
    print(request.GET.get('q'))
    cafe_list = Cafe.objects.filter(name__contains=request.GET.get('q'))
    return HttpResponse(serializers.serialize('json', cafe_list), content_type="application/json")
