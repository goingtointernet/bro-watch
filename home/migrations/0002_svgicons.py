# Generated by Django 4.2.5 on 2023-11-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SvgIcons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('meta_desc', models.CharField(max_length=160)),
                ('meta_key', models.CharField(max_length=260)),
                ('content', models.TextField()),
                ('svg_code', models.TextField()),
                ('slug', models.CharField(max_length=70, unique=True)),
            ],
        ),
    ]