# Generated by Django 5.1.1 on 2024-09-17 02:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_aboutcoachingdetails_accenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurValuesDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('OValues', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.aboutcoachingcenter')),
            ],
        ),
    ]
