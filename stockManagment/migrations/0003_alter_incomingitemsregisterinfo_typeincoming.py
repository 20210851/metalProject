# Generated by Django 4.2.2 on 2023-07-18 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockManagment', '0002_incomingitemsregisterinfo_endpointincoming_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingitemsregisterinfo',
            name='typeIncoming',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
