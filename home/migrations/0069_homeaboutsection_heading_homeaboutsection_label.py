# Generated by Django 4.2.5 on 2024-12-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0068_sitedata_category_section_heading_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeaboutsection',
            name='heading',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='homeaboutsection',
            name='label',
            field=models.TextField(default=''),
        ),
    ]
