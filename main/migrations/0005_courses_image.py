# Generated by Django 3.2.4 on 2021-06-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_lesson_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Images'),
        ),
    ]