# Generated by Django 5.0 on 2023-12-19 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_medeom_products_medeom_medeom_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_medeom',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]
