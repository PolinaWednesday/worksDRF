# Generated by Django 5.0.2 on 2024-03-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_payment_course_alter_payment_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
    ]
