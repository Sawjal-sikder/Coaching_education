from django.shortcuts import render
from .models import *
from django.views.generic import CreateView, UpdateView
from .forms import *
from django.urls import reverse_lazy

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
    all_videos = videos.objects.filter(is_active=True)
    return render(request, 'index.html', {
        'blogs': blogs,
        'aboutfirstcoll': aboutfirstcoll,
        'aboutseceondcoll': aboutseceondcoll,
        'courses': courses,
        'videos': all_videos,
    })


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