import os
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    # return HttpResponse()
    # print(os.getcwd())
    path = os.path.join(os.getcwd(), 'engesep_site', 'static', 'assets')
    slides = [s for s in os.listdir(path) if 'slide' in s]
    # global slides
    print('Ola: ', slides)
    print(round(928/1261,2))
    template = loader.get_template('index.html')
    context = {'slides': slides}
    return HttpResponse(template.render(context, request))




# Create your views here.
