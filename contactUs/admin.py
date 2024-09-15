from django.contrib import admin
from .models import *


@admin.register(companyProfile)
class companyProfileAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'email', ]


@admin.register(feetBack)
class feetBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment', ]
