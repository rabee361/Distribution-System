# Generated by Django 5.0 on 2023-12-26 03:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_alter_codeverification_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeverification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='codeverification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 3, 36, 24, 594355, tzinfo=datetime.timezone.utc)),
        ),
    ]