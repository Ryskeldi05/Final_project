from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Images', blank=True, null=True)


class Modules(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)


class Content_Type(models.Model):
    description = models.CharField(max_length=250)


class Content(models.Model):
    module = models.ForeignKey(Modules, related_name="content", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    text = models.TextField()
    duration = models.CharField(max_length=250)
    content_type = models.ForeignKey(Content_Type, on_delete=models.DO_NOTHING)


class Mentors(models.Model):
    full_name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='Images', blank=True, null=True)



