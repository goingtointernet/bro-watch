# Generated by Django 4.2.5 on 2024-08-07 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_oemcustom_oemcustombox'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitedata',
            old_name='facebook',
            new_name='alibaba',
        ),
        migrations.RenameField(
            model_name='sitedata',
            old_name='instagram',
            new_name='pinterest',
        ),
        migrations.RenameField(
            model_name='sitedata',
            old_name='twitter',
            new_name='tiktok',
        ),
    ]
