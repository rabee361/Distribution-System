# Generated by Django 5.0 on 2024-02-17 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_rename_notifications_notification'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='UserNotification',
        ),
    ]
