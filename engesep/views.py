import os
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings

def index(request):
    # return HttpResponse()
    # path = os.getcwd()
    # print(path)
    print('static url: ', settings.STATIC_URL)
    print('static root: ', settings.STATIC_ROOT)
    print('static dirs: ', settings.STATICFILES_DIRS)
    path = os.environ.get('ASSETS_DIR', os.path.join(settings.STATICFILES_DIRS[0], 'assets'))

    if not os.path.exists(path):
        os.makedirs(path)

    slides = [s for s in os.listdir(path) if 'slide' in s]

    # path = os.path.join(os.getcwd(), 'engesep_site', 'static', 'assets')
    # path = os.path.join(settings.STATICFILES_DIRS[0], 'assets')
    # slides = [s for s in os.listdir(path) if 'slide' in s]
    # global slides
    print('Ola: ', slides)
    print(round(928/1261,2))
    template = loader.get_template('index.html')
    context = {'slides': slides}
    return HttpResponse(template.render(context, request))


