# Generated by Django 2.0.1 on 2018-01-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20180117_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='Acquisitiondate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='Purchasedate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='Returndate',
            field=models.DateField(null=True),
        ),
    ]
