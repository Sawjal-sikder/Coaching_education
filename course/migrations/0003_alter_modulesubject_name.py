# Generated by Django 5.1.1 on 2024-09-15 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_classsubject_modulesubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulesubject',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
