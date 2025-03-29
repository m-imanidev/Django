# Generated by Django 5.1.6 on 2025-03-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_rename_status_author_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'کتاب', 'verbose_name_plural': 'کتاب ها'},
        ),
        migrations.AddField(
            model_name='author',
            name='data_create',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='author',
            name='url',
            field=models.URLField(default='/'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='data_create',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='url',
            field=models.URLField(default='/'),
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
