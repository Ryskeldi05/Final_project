from django.urls import path
from .views import main_page, courses, content, mentors, blog, contact, modules



urlpatterns = [
    path('', main_page, name='main_page'),
    path('courses/', courses, name='courses'),
    path('modules/<int:course_id>/', modules, name='modules'),
    path('content/<int:module_id>/', content, name='content'),
    path('mentors/', mentors, name='mentors'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    ]