# Generated by Django 5.0 on 2023-12-14 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_rename_number_client_phomnenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(null=True, upload_to='images/users'),
        ),
    ]
