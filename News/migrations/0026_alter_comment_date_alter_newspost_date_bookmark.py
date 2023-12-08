# Generated by Django 4.1.7 on 2023-04-02 13:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('News', '0025_alter_comment_date_alter_newspost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 2, 18, 48, 22, 240964)),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 2, 18, 48, 22, 239942)),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.newspost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
