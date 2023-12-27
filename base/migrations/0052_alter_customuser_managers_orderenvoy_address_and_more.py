# Generated by Django 5.0 on 2023-12-27 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0051_alter_codeverification_expires_at_notifications'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='orderenvoy',
            name='address',
            field=models.CharField(default='address', max_length=100),
        ),
        migrations.AlterField(
            model_name='codeverification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 18, 35, 29, 844451, tzinfo=datetime.timezone.utc)),
        ),
    ]
