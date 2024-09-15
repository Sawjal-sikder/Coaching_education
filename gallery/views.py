from django.shortcuts import render
from .models import *


# Create your views here.
def galleryView(request):
    context = {
        'galleries': Gallery.objects.filter(is_active=True)
    }
    return render(request, 'gallery.html', context)
