from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'titleTwo', ]


@admin.register(About_coching)
class About_cochingAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', ]
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription','is_active' ]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription','is_active' ]


@admin.register(videos)
class videosAdmin(admin.ModelAdmin):
    list_display = ['title', ]

@admin.register(faq)
class faqAdmin(admin.ModelAdmin):
    list_display = ['title','slug',]
    prepopulated_fields = {'slug':('title',)}

@admin.register(faq_details)
class faq_detailsAdmin(admin.ModelAdmin):
    list_display = ['faq_title','question','answer']
@admin.register(studentRegistration)
class studentRegistrationAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','mobile_number']


