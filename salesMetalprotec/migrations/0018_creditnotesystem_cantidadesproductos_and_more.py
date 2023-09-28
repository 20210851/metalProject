# Generated by Django 4.2 on 2023-09-08 17:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesMetalprotec', '0017_creditnotesystem_creditnotepurpose'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnotesystem',
            name='cantidadesProductos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=12), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='creditnotesystem',
            name='codigosProductos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, null=True, size=None),
        ),
    ]