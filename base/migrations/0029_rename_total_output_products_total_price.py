# Generated by Django 5.0 on 2024-01-08 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_alter_incoming_product_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='output_products',
            old_name='total',
            new_name='total_price',
        ),
    ]