# Generated by Django 4.2.5 on 2024-05-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_category_category_banner_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedata',
            name='home_banner',
            field=models.ImageField(blank=True, null=True, upload_to='Home'),
        ),
    ]
