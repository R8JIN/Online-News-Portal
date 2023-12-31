# Generated by Django 4.1.7 on 2023-03-24 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0012_alter_newspost_options_remove_newspost_subcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 24, 22, 8, 2, 475964)),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='News/categories'),
        ),
    ]
