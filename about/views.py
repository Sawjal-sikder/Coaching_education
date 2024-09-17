from django.shortcuts import render
from .models import *


# Create your views here.
def aboutCoachinCenter(request):
    abouts = AboutCoachingCenter.objects.all()
    context = {
        'abouts': abouts,
    }
    return render(request, 'aboutCoachingC.html', context)


def ourvalues(request):
    values = OurValues.objects.all()
    context = {
        'values': values,
    }
    return render(request, 'our_values.html', context)
