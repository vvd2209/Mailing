# Generated by Django 4.2.7 on 2024-01-28 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_message_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='owner',
        ),
    ]