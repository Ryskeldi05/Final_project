from django.shortcuts import render
from .models import Courses, Modules, Lesson, Content_Type, Content



def main_page(request):
    return render(request, 'index.html', {'main_page': main_page})

def courses (request):
    courses = Courses.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def modules (request):
    modules = Modules.objects.all()
    return render(request, 'modules.html', {'modules': modules})

def lesson (request):
    lesson = Lesson.objects.all()
    return render(request, 'lesson.html', {'lesson': lesson})

def content_type (request):
    content_type = Content_Type.objects.all()
    return render(request, 'content_type.html', {'content_type': content_type})

def content (request):
    content = Content.objects.all()
    return render(request, 'content.html', {'content': content})

def mentors (request):
    return render(request, 'mentors.html', {'mentors': mentors})

def blog (request):
    return render(request, 'blog.html', {'blog': blog})

def contact (request):
    return render(request, 'contact.html', {'contact': contact})
