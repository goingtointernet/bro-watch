# Generated by Django 4.2.5 on 2024-08-12 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0060_alter_sitedata_nav_products_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeaboutsection',
            name='heading',
        ),
    ]
