# Generated by Django 4.2 on 2024-09-08 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrencytransaction',
            name='amount_of_bought_currency',
            field=models.DecimalField(decimal_places=9, max_digits=16),
        ),
    ]
