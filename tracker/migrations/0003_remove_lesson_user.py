# Generated by Django 5.0.2 on 2024-03-07 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_course_user_lesson_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='user',
        ),
    ]
