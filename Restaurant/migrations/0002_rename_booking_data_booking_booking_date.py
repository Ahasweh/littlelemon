# Generated by Django 4.2.5 on 2023-09-18 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_data',
            new_name='booking_date',
        ),
    ]
