# Generated by Django 5.1.7 on 2025-03-11 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_publisher_book_inventory_book_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
