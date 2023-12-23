# Generated by Django 4.2.8 on 2023-12-23 09:48

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_rename_phomnenumber_client_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediumTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='num',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='AE'),
        ),
        migrations.CreateModel(
            name='MediumTwo_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('mediumtwo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.mediumtwo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
        migrations.AddField(
            model_name='mediumtwo',
            name='products',
            field=models.ManyToManyField(through='base.MediumTwo_Products', to='base.product'),
        ),
    ]
