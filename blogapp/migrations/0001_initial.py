# Generated by Django 4.0.5 on 2022-07-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=40)),
                ('Choose_Image', models.ImageField(upload_to='images')),
                ('Description', models.TextField(max_length=10000)),
                ('Your_Name', models.CharField(max_length=40)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.BigIntegerField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
