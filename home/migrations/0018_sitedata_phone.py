# Generated by Django 4.2.5 on 2024-05-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_sitedata_group_desc_sitedata_group_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedata',
            name='phone',
            field=models.CharField(default='', max_length=160),
        ),
    ]