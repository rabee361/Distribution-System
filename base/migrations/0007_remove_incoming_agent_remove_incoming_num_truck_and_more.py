# Generated by Django 5.0 on 2024-01-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_salary_options_alter_employee_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incoming',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='incoming',
            name='num_truck',
        ),
        migrations.AlterField(
            model_name='incoming',
            name='Reclaimed_products',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='discount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='previous_depts',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='remaining_amount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='manualreceipt',
            name='previous_depts',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='manualreceipt',
            name='reclaimed_products',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='manualreceipt',
            name='remaining_amount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='Reclaimed_products',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='discount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='previous_depts',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='output',
            name='remaining_amount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_per_carton',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='num_per_item',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
