from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # static(settings.STATIC_URL)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# for url in settings:
#     print(url)
print('Urls app 1: ',settings.STATIC_URL)
print('Urls app 2: ',settings.STATICFILES_DIRS)
