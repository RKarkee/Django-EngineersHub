# Generated by Django 2.2.3 on 2019-07-07 19:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0003_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
