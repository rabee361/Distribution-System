# Generated by Django 4.2.8 on 2023-12-23 10:42

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_alter_num_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='num',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='DZ'),
        ),
    ]