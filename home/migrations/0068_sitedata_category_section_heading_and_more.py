# Generated by Django 4.2.5 on 2024-08-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0067_rename_star_banner_image_aboutpage_start_banner_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedata',
            name='category_section_heading',
            field=models.CharField(default='', max_length=260),
        ),
        migrations.AddField(
            model_name='sitedata',
            name='category_section_paragraph',
            field=models.CharField(default='', max_length=260),
        ),
    ]
