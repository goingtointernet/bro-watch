# Generated by Django 4.2.5 on 2024-07-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_newsposts_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsposts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]