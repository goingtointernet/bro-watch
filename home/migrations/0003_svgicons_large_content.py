# Generated by Django 4.2.5 on 2023-11-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_svgicons'),
    ]

    operations = [
        migrations.AddField(
            model_name='svgicons',
            name='large_content',
            field=models.TextField(default=''),
        ),
    ]
