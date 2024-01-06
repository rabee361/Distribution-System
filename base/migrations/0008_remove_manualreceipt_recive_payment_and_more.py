# Generated by Django 5.0 on 2024-01-05 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_incoming_agent_remove_incoming_num_truck_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manualreceipt',
            name='recive_payment',
        ),
        migrations.AlterField(
            model_name='incoming',
            name='remaining_amount',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='manualreceipt',
            name='remaining_amount',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]