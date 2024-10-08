# Generated by Django 5.1.1 on 2024-09-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_faq_is_active_faq_details_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=11, unique=True)),
            ],
        ),
    ]
