# Generated by Django 4.1.2 on 2023-03-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
