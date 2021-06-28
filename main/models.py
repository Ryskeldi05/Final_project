from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Images', blank=True, null=True)



class Modules(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)




class Lesson(models.Model):
    models_id = models.ForeignKey(Modules, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)




class Content_Type(models.Model):
    description = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)





class Content(models.Model):
    lesson_id = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    content_type = models.ForeignKey(Content_Type,on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Images', blank=True, null=True)









