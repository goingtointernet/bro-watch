# Generated by Django 4.2.5 on 2024-08-19 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0065_aboutpage_customerbox'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerbox',
            old_name='customer_boxe',
            new_name='customer_box',
        ),
    ]
