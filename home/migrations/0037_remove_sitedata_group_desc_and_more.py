# Generated by Django 4.2.5 on 2024-05-21 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_sitedata_whatsapp_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitedata',
            name='group_desc',
        ),
        migrations.RemoveField(
            model_name='sitedata',
            name='group_heading',
        ),
        migrations.RemoveField(
            model_name='sitedata',
            name='group_key',
        ),
    ]