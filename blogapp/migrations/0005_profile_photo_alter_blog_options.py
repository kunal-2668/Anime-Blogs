# Generated by Django 4.1.2 on 2022-12-17 08:55

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0004_alter_blog_choose_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile_photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=255)),
                (
                    "profile",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="image"
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ["-time"]},
        ),
    ]
