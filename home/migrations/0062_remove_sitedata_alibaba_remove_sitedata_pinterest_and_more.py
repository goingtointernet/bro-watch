# Generated by Django 4.2.5 on 2024-08-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_remove_homeaboutsection_heading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitedata',
            name='alibaba',
        ),
        migrations.RemoveField(
            model_name='sitedata',
            name='pinterest',
        ),
        migrations.RemoveField(
            model_name='sitedata',
            name='tiktok',
        ),
        migrations.AddField(
            model_name='sitedata',
            name='store_available_time',
            field=models.CharField(default='', max_length=160),
        ),
    ]