# Generated by Django 4.2.7 on 2024-01-31 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_mailing_day_mailing_day_week_alter_mailing_clients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='day',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='day_week',
        ),
    ]