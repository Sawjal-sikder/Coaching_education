# Generated by Django 5.1.1 on 2024-09-15 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactUs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
