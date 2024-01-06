# Generated by Django 5.0 on 2024-01-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_client_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt_client',
            name='receipt_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='debt_supplier',
            name='check_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='verify_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='receipt_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='receipt_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recieved_payment',
            name='receipt_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='verify_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
