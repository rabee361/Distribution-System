# Generated by Django 4.2.10 on 2024-02-22 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clients_and_Products', '0020_alter_product_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.producttype'),
        ),
    ]