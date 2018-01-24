# Generated by Django 2.0.1 on 2018-01-17 07:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='type',
            new_name='Type',
        ),
        migrations.AddField(
            model_name='computer',
            name='Acquisitiondate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='Assetownedby',
            field=models.CharField(choices=[('legend', 'Legend'), ('rental', 'Rental')], default='Legend', max_length=8),
        ),
        migrations.AddField(
            model_name='computer',
            name='Barcode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='CPU',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='Desknumber',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='computer',
            name='Domain',
            field=models.CharField(choices=[('corp', 'Corp'), ('prod', 'Prod')], default='Prod', max_length=10),
        ),
        migrations.AddField(
            model_name='computer',
            name='EndofLife',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='ExternalStorage',
            field=models.CharField(default='1 TB', max_length=50),
        ),
        migrations.AddField(
            model_name='computer',
            name='GPU',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='Invoicenumber',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='Location',
            field=models.CharField(default='Pune', max_length=50),
        ),
        migrations.AddField(
            model_name='computer',
            name='Make',
            field=models.CharField(default='DELL', max_length=30),
        ),
        migrations.AddField(
            model_name='computer',
            name='Modelnumber',
            field=models.CharField(default='7810', max_length=20),
        ),
        migrations.AddField(
            model_name='computer',
            name='OS',
            field=models.CharField(choices=[('window', 'Windows'), ('linux', 'Linux')], default='Windows', max_length=20),
        ),
        migrations.AddField(
            model_name='computer',
            name='Purchasedate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='computer',
            name='Ram',
            field=models.CharField(default='64 GB', max_length=50),
        ),
        migrations.AddField(
            model_name='computer',
            name='Returndate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='SerialNo',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='ServiceNo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='Status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('decommissioned', 'Decommissioned'), ('return', 'Return')], default='Active', max_length=20),
        ),
        migrations.AddField(
            model_name='computer',
            name='Warranty',
            field=models.CharField(default='1 Year', max_length=20),
        ),
        migrations.AddField(
            model_name='computer',
            name='WorkstationName',
            field=models.CharField(default='Name', max_length=150),
        ),
    ]