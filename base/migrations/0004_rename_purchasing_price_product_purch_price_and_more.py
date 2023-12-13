# Generated by Django 5.0 on 2023-12-13 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='purchasing_price',
            new_name='purch_price',
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='iamge',
            field=models.ImageField(upload_to='images\\poduct'),
        ),
    ]
