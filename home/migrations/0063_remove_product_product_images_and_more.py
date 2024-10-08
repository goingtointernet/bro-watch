# Generated by Django 4.2.5 on 2024-08-13 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0062_remove_sitedata_alibaba_remove_sitedata_pinterest_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_show_images',
        ),
        migrations.AddField(
            model_name='productimages',
            name='heading',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='home.product'),
        ),
        migrations.AddField(
            model_name='productshowimages',
            name='heading',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_show_images', to='home.product'),
        ),
    ]
