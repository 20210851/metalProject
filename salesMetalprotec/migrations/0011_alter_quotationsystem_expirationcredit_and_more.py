# Generated by Django 4.2.2 on 2023-07-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesMetalprotec', '0010_alter_billsystem_statetefacturo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationsystem',
            name='expirationCredit',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='quotationsystem',
            name='expirationQuotation',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='quotationsystem',
            name='quotesQuotation',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]