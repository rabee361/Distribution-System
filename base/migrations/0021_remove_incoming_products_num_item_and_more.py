# Generated by Django 5.0 on 2023-12-15 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_employee_incoming_incoming_products_incoming_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incoming_products',
            name='num_item',
        ),
        migrations.RemoveField(
            model_name='incoming_products',
            name='purch_price',
        ),
    ]