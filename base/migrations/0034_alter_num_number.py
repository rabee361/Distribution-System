# Generated by Django 4.2.8 on 2023-12-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_num_orderenvoy_product_order_envoy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='num',
            name='number',
            field=models.PositiveBigIntegerField(),
        ),
    ]