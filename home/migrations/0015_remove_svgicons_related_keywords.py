# Generated by Django 4.2.5 on 2024-03-17 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_svgicons_icon_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='svgicons',
            name='related_keywords',
        ),
    ]