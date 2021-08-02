from django.contrib import admin
from .models import Courses, Modules, Content_Type, Content,Mentors, Blog



# Register your mod
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'duration', 'image']


@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Content_Type)
class Content_typeAdmin(admin.ModelAdmin):
    list_display = ['description']


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'duration']



@admin.register(Mentors)
class MentorsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'description', 'image']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'image']