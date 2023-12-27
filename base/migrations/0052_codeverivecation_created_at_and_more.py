# Generated by Django 4.2.8 on 2023-12-24 10:00

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0051_mediumtwo_orderenvoy_product_order_envoy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='codeverivecation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codeverivecation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 10, 13, 59, 858116, tzinfo=datetime.timezone.utc)),
        ),
    ]