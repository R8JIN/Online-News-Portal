# Generated by Django 4.1.7 on 2023-03-28 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0016_alter_newspost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 28, 9, 45, 45, 652156)),
        ),
    ]
