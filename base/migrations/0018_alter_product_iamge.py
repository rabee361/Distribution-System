# Generated by Django 5.0 on 2023-12-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='iamge',
            field=models.ImageField(upload_to='images\\product'),
        ),
    ]
