from django.contrib import admin
from .models import Courses, Modules, Lesson, Content_Type, Content



# Register your mod
admin.site.register(Courses)
admin.site.register(Modules)
admin.site.register(Lesson)
admin.site.register(Content_Type)
admin.site.register(Content)