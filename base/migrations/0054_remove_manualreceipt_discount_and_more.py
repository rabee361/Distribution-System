# Generated by Django 5.0 on 2024-01-02 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0053_rename_discount_products_medium_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manualreceipt',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='manualreceipt_products',
            name='discount',
        ),
        migrations.AlterField(
            model_name='codeverification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 11, 31, 20, 850570, tzinfo=datetime.timezone.utc)),
        ),
    ]