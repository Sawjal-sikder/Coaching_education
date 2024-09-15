from django.urls import path
from .views import *

urlpatterns = [
    path('', galleryView, name="gallery")
]
