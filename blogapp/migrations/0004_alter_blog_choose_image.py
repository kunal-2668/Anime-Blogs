# Generated by Django 4.1.2 on 2022-12-06 05:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Choose_Image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
