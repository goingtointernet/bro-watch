# Generated by Django 4.2.5 on 2024-02-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_homegroups_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homegroups',
            name='slug',
            field=models.CharField(default='', max_length=70, unique=True),
        ),
    ]