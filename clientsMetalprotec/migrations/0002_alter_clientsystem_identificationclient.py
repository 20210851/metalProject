# Generated by Django 4.2.2 on 2023-07-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientsMetalprotec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsystem',
            name='identificationClient',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
