# Generated by Django 2.2 on 2020-07-16 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='slug',
        ),
    ]
