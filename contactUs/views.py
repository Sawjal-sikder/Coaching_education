from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


# Create your views here.

def contactUs(request):
    context = {
        'profiles': companyProfile.objects.filter(is_active=True),
    }
    return render(request, 'contactUs.html', context)


def feetBackview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        profile = feetBack.objects.create(name=name, email=email, comment=comment)
        profile.save()
        messages.success(request, 'Thank you for your feedback! We appreciate your input.')
        return redirect('contactUs')
