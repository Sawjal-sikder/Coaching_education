from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(AboutCoachingCenter)
class AboutCoachingCenterAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(AboutCoachingDetails)
class AboutCoachingDetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(OurValues)
class OurValuesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(OurValuesDetails)
class OurValuesDetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


