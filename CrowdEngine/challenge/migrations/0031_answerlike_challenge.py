# Generated by Django 2.2 on 2020-08-24 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0030_auto_20200823_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerlike',
            name='challenge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge', to='challenge.Challenge'),
        ),
    ]
