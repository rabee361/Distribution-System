# Generated by Django 5.0 on 2024-01-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_debt_client_receipt_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualreceipt',
            name='recive_payment',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]