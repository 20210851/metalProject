# Generated by Django 4.2 on 2023-08-23 13:29

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settingsMetalprotec', '0001_initial'),
        ('expensesMetalprotec', '0003_boxregister_costregister_cashincome'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordenCompraMetalprotec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rucProveedor', models.CharField(blank=True, max_length=32, null=True)),
                ('fechaEmision', models.DateField(blank=True, null=True)),
                ('condicionOrden', models.CharField(blank=True, max_length=32, null=True)),
                ('codigoOrden', models.CharField(blank=True, max_length=32, null=True)),
                ('direccionProveedor', models.CharField(blank=True, max_length=128, null=True)),
                ('nombreProveedor', models.CharField(blank=True, max_length=64, null=True)),
                ('ciudadCliente', models.CharField(blank=True, max_length=32, null=True)),
                ('destinoCliente', models.CharField(blank=True, max_length=128, null=True)),
                ('atencionCliente', models.CharField(blank=True, max_length=64, null=True)),
                ('monedaOrden', models.CharField(blank=True, max_length=12, null=True)),
                ('productosOrden', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), blank=True, null=True, size=None), blank=True, null=True, size=None)),
                ('tcCompraOrden', models.CharField(blank=True, max_length=8, null=True)),
                ('tcVentaOrden', models.CharField(blank=True, max_length=8, null=True)),
                ('mostrarDescuento', models.CharField(blank=True, max_length=8, null=True)),
                ('mostrarVU', models.CharField(blank=True, max_length=8, null=True)),
                ('endpointOrden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settingsMetalprotec.endpointsystem')),
            ],
        ),
    ]
