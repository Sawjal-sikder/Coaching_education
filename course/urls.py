from django.urls import path
from .views import *

urlpatterns = [
    path('details/<slug:slug>', courseView, name='courseurl'),
    path('registration/', courseRegistration, name='registration')
]
