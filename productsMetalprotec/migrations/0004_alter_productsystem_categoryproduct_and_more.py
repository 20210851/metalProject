# Generated by Django 4.2.2 on 2023-07-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsMetalprotec', '0003_productsystem_kitinfo_productsystem_kitproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsystem',
            name='categoryProduct',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='productsystem',
            name='subCategoryProduct',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
