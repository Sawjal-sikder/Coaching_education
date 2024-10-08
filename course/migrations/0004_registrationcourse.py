# Generated by Django 5.1.1 on 2024-09-15 22:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_modulesubject_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]
