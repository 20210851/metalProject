# Generated by Django 4.2 on 2023-10-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesMetalprotec', '0018_creditnotesystem_cantidadesproductos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guidesystem',
            name='stateDiscount',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
