# Generated by Django 5.1.6 on 2025-03-15 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_options_author_data_create_author_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='Active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Inventory',
            new_name='inventory',
        ),
        migrations.RenameField(
            model_name='publisher',
            old_name='Active',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='author',
            name='data_create',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='books.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='books.publisher'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='data_create',
            field=models.DateField(auto_now=True),
        ),
    ]
