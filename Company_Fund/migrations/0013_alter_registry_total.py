# Generated by Django 5.0 on 2024-03-16 19:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Fund', '0012_alter_debt_client_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='total',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
