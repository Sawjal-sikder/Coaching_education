from django.shortcuts import render, redirect
from .models import *
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import *
from django.urls import reverse_lazy
from contactUs.models import *


# Create your views here.
def indexView(request):
    # Slider Section
    blogs = Blog.objects.filter(is_active=True)
    # About section
    aboutfirstcoll = About_coching.objects.all()[:2]
    aboutseceondcoll = About_coching.objects.all()[2:4]
    # Course Section
    courses = Course.objects.filter(is_active=True)
    # Videos Section
    single_video = videos.objects.filter(is_active=True)[:1]
    all_videos = videos.objects.filter(is_active=True)
    single_faq = faq.objects.filter(is_active=True)
    # map Section
    profiles = companyProfile.objects.filter(is_active=True)
    return render(request, 'index.html', {
        'blogs': blogs,
        'aboutfirstcoll': aboutfirstcoll,
        'aboutseceondcoll': aboutseceondcoll,
        'courses': courses,
        'videos': single_video,
        'all_videos': all_videos,
        'faqs': single_faq,
        'profiles': profiles,
    })

class faq_details(DetailView):
    model = faq
    template_name = 'faqs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = faq.objects.filter(is_active=True)  # You can filter other FAQs if needed
        return context


def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        print(first_name)
        # Check if required fields are provided
        if not first_name or not last_name or not email:
            return render(request, 'faqs.html', {'error': 'Please fill out all required fields.'})

        # Check if email is already registered
        if studentRegistration.objects.filter(email=email).exists():
            return render(request, 'faqs.html', {'error': 'Email is already registered.'})

        # Create and save the new studentRegistration instance
        reg = studentRegistration.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_number=mobile_number
        )
        reg.save()
        return redirect('index')





class AboutCreateView(CreateView):
    model = About_coching
    form_class = AboutForm
    template_name = 'form/CreateAbout.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AboutUpdateView(UpdateView):
    model = About_coching
    form_class = AboutForm
    template_name = 'form/UpdateAbout.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
