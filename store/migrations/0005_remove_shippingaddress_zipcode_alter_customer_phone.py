# Generated by Django 4.1 on 2022-11-27 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]
