# Generated by Django 4.2 on 2023-07-30 02:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeMetalprotec', '0005_settingscomission_asociatedusercomission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingscomission',
            name='asociatedUsers',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=8), blank=True, null=True, size=None), blank=True, null=True, size=None),
        ),
    ]
