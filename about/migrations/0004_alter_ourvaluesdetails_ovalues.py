# Generated by Django 5.1.1 on 2024-09-17 23:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_ourvalues_ourvaluesdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourvaluesdetails',
            name='OValues',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='about.aboutcoachingcenter'),
        ),
    ]
