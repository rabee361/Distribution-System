# Generated by Django 4.2.10 on 2024-02-09 05:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Clients_and_Products', '0012_alter_order_total_points_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='barcode',
            field=models.CharField(default=uuid.uuid4, max_length=200),
        ),
    ]
