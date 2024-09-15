# Generated by Django 5.1.1 on 2024-09-15 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='gallery/photos/')),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='photo',
        ),
        migrations.AddField(
            model_name='gallery',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
