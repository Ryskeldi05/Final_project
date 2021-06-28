from django.urls import path
from .views import main_page, courses, content, mentors, blog, contact



urlpatterns = [
    path('', main_page, name='main_page'),
    path('courses/', courses, name='courses'),
    path('content/', content, name='content'),
    path('mentors/', mentors, name='mentors'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact')
    ]