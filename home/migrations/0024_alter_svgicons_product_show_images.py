# Generated by Django 4.2.5 on 2024-05-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_svgicons_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='svgicons',
            name='product_show_images',
            field=models.ManyToManyField(to='home.productshowimages'),
        ),
    ]