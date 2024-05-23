# Generated by Django 4.0.4 on 2024-03-20 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_sitedata_group_heading_sitedata_search_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedata',
            name='group_desc',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AddField(
            model_name='sitedata',
            name='group_key',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AddField(
            model_name='sitedata',
            name='search_desc',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AddField(
            model_name='sitedata',
            name='search_key',
            field=models.CharField(default='', max_length=160),
        ),
    ]