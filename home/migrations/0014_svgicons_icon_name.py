# Generated by Django 4.2.5 on 2024-03-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_homegroups_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='svgicons',
            name='icon_name',
            field=models.CharField(default='', max_length=260),
        ),
    ]
