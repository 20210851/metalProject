# Generated by Django 4.2.2 on 2023-07-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockManagment', '0003_alter_incomingitemsregisterinfo_typeincoming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingitemsregisterinfo',
            name='lastStock',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='incomingitemsregisterinfo',
            name='nameStore',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='incomingitemsregisterinfo',
            name='newStock',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='incomingitemsregisterinfo',
            name='quantityProduct',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='incomingitemsregisterinfo',
            name='referenceIncome',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]