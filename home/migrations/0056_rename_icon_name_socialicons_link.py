# Generated by Django 4.2.5 on 2024-08-12 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_navmenu_socialicons_sitedata_menu_list_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialicons',
            old_name='icon_name',
            new_name='link',
        ),
    ]