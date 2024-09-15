from django.urls import path
from .views import *

urlpatterns = [
    path('', contactUs, name="contactUs"),
    path('feetback', feetBackview, name="feetBack")
]
