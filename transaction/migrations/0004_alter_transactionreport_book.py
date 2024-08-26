# Generated by Django 5.0.4 on 2024-08-22 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_books_categories_books_categories'),
        ('transaction', '0003_alter_transactionreport_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionreport',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.books'),
        ),
    ]
