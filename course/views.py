from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def courseView(request, slug):
    courseDetail = Course.objects.get(slug=slug)
    classSubjects = classSubject.objects.get(course_title=courseDetail)
    ModuleSubjects = ModuleSubject.objects.filter(course_title=classSubjects)
    context = {
        'courseDetail': courseDetail,
        'classSubjects': classSubjects,
        'ModuleSubjects': ModuleSubjects,
    }
    return render(request, 'course_details.html', context)


def courseRegistration(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the registration data
            return redirect('index')  # Redirect after successful form submission
    else:
        form = registrationForm()


    return render(request, 'studen_registration.html', {'form':form})
