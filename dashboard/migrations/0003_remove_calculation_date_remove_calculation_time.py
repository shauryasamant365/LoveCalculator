# Generated by Django 4.1.4 on 2023-04-28 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_calculations_calculation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculation',
            name='date',
        ),
        migrations.RemoveField(
            model_name='calculation',
            name='time',
        ),
    ]