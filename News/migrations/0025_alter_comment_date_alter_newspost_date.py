# Generated by Django 4.1.7 on 2023-03-31 05:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0024_alter_comment_date_alter_newspost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 31, 10, 48, 29, 417833)),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 31, 10, 48, 29, 417833)),
        ),
    ]
