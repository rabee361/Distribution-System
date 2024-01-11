# Generated by Django 4.2.8 on 2023-12-24 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0055_alter_codeverivecation_expires_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='clinet',
            new_name='client',
        ),
        migrations.AlterField(
            model_name='codeverivecation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 11, 32, 57, 719503, tzinfo=datetime.timezone.utc)),
        ),
    ]