from django.urls import path
from .views import *

urlpatterns = [
    path('', aboutCoachinCenter, name='aboutCoachinCenter'),
    path('our/values/', ourvalues, name='ourvalues'),
]
