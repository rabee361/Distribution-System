# Generated by Django 5.0 on 2024-03-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Human_Resources', '0008_employee_phonenumber2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='percentage',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
