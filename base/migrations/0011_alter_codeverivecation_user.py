# Generated by Django 5.0 on 2023-12-13 22:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_codeverivecation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeverivecation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
