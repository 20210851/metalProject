# Generated by Django 4.2.2 on 2023-07-10 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settingsMetalprotec', '0001_initial'),
        ('salesMetalprotec', '0002_billsystem_quotationproductdata_weightproduct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billsystem',
            name='codeBill',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='creditnotesystem',
            name='codeCreditNote',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='creditnotesystem',
            name='endpointGuide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settingsMetalprotec.endpointsystem'),
        ),
        migrations.AddField(
            model_name='guidesystem',
            name='codeGuide',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='invoicesystem',
            name='codeInvoice',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
