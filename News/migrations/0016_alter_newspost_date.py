# Generated by Django 4.1.7 on 2023-03-27 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0015_alter_newspost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 27, 13, 42, 35, 456368)),
        ),
    ]
