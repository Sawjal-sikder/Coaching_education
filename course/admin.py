from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(classSubject)
class classSubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active']


@admin.register(ModuleSubject)
class ModuleSubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active']


@admin.register(RegistrationCourse)
class RegistrationCourseAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'course', ]
