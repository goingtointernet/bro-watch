# Generated by Django 4.2.5 on 2024-07-31 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_oem_main_heading_alter_oem_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='OemCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(null=True, upload_to='oemodm')),
                ('heading', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='OemCustomBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=260)),
                ('text', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='oemodm')),
                ('main_heading', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='oemcustombox', to='home.oemcustom')),
            ],
        ),
    ]