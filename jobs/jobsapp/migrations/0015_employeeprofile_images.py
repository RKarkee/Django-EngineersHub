# Generated by Django 2.2.2 on 2019-07-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0014_employeeprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='images',
            field=models.ImageField(default='default.jpg', upload_to='employeeProfiles'),
        ),
    ]
