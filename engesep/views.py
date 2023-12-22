import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    # return HttpResponse()
    print(os.getcwd())
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))




# Create your views here.
