from django.contrib import admin
from .models import Courses, Modules, Content_Type, Content,Mentors



# Register your mod
admin.site.register(Courses)
admin.site.register(Modules)
admin.site.register(Content_Type)
admin.site.register(Content)
admin.site.register(Mentors)