from django.shortcuts import render
from .models import Courses, Modules, Content_Type, Content, Mentors



def main_page(request):
    return render(request, 'index.html', {'main_page': main_page})

def courses (request):
    courses = Courses.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def modules (request,course_id):
    modules = Modules.objects.filter(course_id__id=course_id)
    return render(request, 'modules.html', {'modules': modules})

def content_type (request):
    content_type = Content_Type.objects.all()
    return render(request, 'content_type.html', {'content_type': content_type})

def content (request, course_id):
    content = Courses.objects.filter(id=course_id)
    return render(request, 'content.html', {'content': content})

def mentors (request):
    mentors = Mentors.objects.all()
    return render(request, 'mentors.html', {'mentors': mentors})

def blog (request):
    return render(request, 'blog.html', {'blog': blog})

def contact (request):
    return render(request, 'contact.html', {'contact': contact})
