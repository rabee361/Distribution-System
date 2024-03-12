# Generated by Django 5.0 on 2024-03-12 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Human_Resources', '0007_alter_employee_phonenumber'),
        ('base', '0033_alter_damagedpackage_employee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='damagedproduct',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='returnedgoodsclient',
            name='employee',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Human_Resources.employee'),
            preserve_default=False,
        ),
    ]
