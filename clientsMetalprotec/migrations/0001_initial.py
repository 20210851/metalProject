# Generated by Django 4.2.2 on 2023-07-05 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settingsMetalprotec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentClient', models.CharField(blank=True, max_length=12, null=True)),
                ('identificationClient', models.CharField(blank=True, max_length=64, null=True)),
                ('typeClient', models.CharField(blank=True, max_length=10, null=True)),
                ('emailClient', models.CharField(blank=True, max_length=48, null=True)),
                ('contactClient', models.CharField(blank=True, max_length=64, null=True)),
                ('phoneClient', models.CharField(blank=True, max_length=16, null=True)),
                ('legalAddressClient', models.CharField(blank=True, max_length=256, null=True)),
                ('enabledCommission', models.CharField(blank=True, max_length=6, null=True)),
                ('endpointClient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settingsMetalprotec.endpointsystem')),
            ],
        ),
        migrations.CreateModel(
            name='addressClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryAddress', models.CharField(blank=True, max_length=256, null=True)),
                ('asociatedClient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientsMetalprotec.clientsystem')),
            ],
        ),
    ]
