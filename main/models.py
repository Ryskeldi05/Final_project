from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Images', blank=True, null=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Modules(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'


class Content_Type(models.Model):
    description = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Тип контента'
        verbose_name_plural = 'Типы контента'


class Content(models.Model):
    module = models.ForeignKey(Modules, related_name="content", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    text = models.TextField()
    duration = models.CharField(max_length=250)
    content_type = models.ForeignKey(Content_Type, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контенты'


class Mentors(models.Model):
    courses = models.ManyToManyField(Courses)
    full_name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='Images', blank=True, null=True)

    class Meta:
        verbose_name = 'Ментор'
        verbose_name_plural = 'Менторы'


class Blog(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to='Images',blank=True, null=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'



