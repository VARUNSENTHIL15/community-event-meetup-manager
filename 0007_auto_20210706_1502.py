# Generated by Django 3.1.4 on 2021-07-06 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community_event_manager', '0006_auto_20210706_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community_event_manager',
            old_name='email_address',
            new_name='contributor',
        ),
    ]
