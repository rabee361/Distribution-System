# Generated by Django 5.0 on 2024-02-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Fund', '0005_deposite_registry'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='added_to_registry',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='added_to_registry',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='recieved_payment',
            name='added_to_registry',
            field=models.BooleanField(default=True),
        ),
    ]