# Generated by Django 4.2.2 on 2023-07-16 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesMetalprotec', '0011_alter_quotationsystem_expirationcredit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationsystem',
            name='relatedDocumentQuotation',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
