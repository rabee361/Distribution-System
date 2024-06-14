# Generated by Django 5.0 on 2024-06-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Human_Resources', '0013_alter_employee_phonenumber_and_more'),
        ('Receipts', '0021_alter_manualreceipt_remaining_amount'),
        ('base', '0054_remove_usernotification_info_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DelievaryArrived',
            new_name='Delivery',
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='details',
            field=models.JSONField(default=dict),
        ),
    ]
