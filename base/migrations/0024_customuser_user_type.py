# Generated by Django 5.0 on 2023-12-22 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.usertype'),
        ),
    ]
