# Generated by Django 5.0.4 on 2024-08-20 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='banalce',
            new_name='balance',
        ),
        migrations.RemoveField(
            model_name='account',
            name='books',
        ),
    ]
