# Generated by Django 5.0 on 2023-12-19 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_products_medeom_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products_medeom',
            name='medeom',
        ),
        migrations.RemoveField(
            model_name='medium',
            name='products',
        ),
        migrations.RemoveField(
            model_name='medium_incoming',
            name='product',
        ),
        migrations.RemoveField(
            model_name='products_medeom',
            name='product',
        ),
        migrations.DeleteModel(
            name='Medeom',
        ),
        migrations.DeleteModel(
            name='Medium',
        ),
        migrations.DeleteModel(
            name='Medium_Incoming',
        ),
        migrations.DeleteModel(
            name='Products_Medeom',
        ),
    ]
