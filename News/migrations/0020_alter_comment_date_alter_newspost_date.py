# Generated by Django 4.1.7 on 2023-03-31 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0019_alter_comment_date_alter_newspost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 31, 10, 10, 20, 663950)),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 31, 10, 10, 20, 663950)),
        ),
    ]