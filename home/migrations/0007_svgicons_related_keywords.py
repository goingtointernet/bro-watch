# Generated by Django 4.2.5 on 2024-02-06 13:23

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_category_svgicons_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='svgicons',
            name='related_keywords',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
