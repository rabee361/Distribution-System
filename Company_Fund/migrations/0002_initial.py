# Generated by Django 5.0 on 2024-01-10 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients_and_Products', '0001_initial'),
        ('Company_Fund', '0001_initial'),
        ('Human_Resources', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt_supplier',
            name='supplier_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.supplier'),
        ),
        migrations.AddField(
            model_name='deposite',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.client'),
        ),
        migrations.AddField(
            model_name='payment',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Human_Resources.employee'),
        ),
        migrations.AddField(
            model_name='recieved_payment',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Human_Resources.employee'),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.client'),
        ),
    ]
