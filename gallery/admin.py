from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', ]
    prepopulated_fields = {'slug': ('title',)}
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'slug', ]
    prepopulated_fields = {'slug': ('title',)}
