from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name='index'),
    path('createAbout/', AboutCreateView.as_view(), name='createAbout'),
    path('UpdateAbout/<int:pk>/', AboutUpdateView.as_view(), name='UpdateAbout'),
]
