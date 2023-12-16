# Generated by Django 5.0 on 2023-12-15 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_incoming_products_num_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming',
            name='agent',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='code_verefy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='discount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.employee'),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='num_truck',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='previous_depts',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='recive_pyement',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.supplier'),
        ),
    ]