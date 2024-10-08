# Generated by Django 5.1.1 on 2024-09-15 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='company/thumbnails/')),
                ('map_link', models.URLField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.URLField(blank=True, max_length=255, null=True)),
                ('twitter', models.URLField(blank=True, max_length=255, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=255, null=True)),
                ('google', models.URLField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='feetBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
            ],
        ),
    ]
