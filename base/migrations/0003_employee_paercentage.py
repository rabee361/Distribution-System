# Generated by Django 5.0 on 2023-12-19 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_medium_discount_remove_medium_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='paercentage',
            field=models.FloatField(default=0.0),
        ),
    ]
