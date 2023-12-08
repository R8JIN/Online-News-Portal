# Generated by Django 4.1.7 on 2023-03-31 04:02

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('News', '0017_alter_newspost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 31, 9, 47, 55, 291129)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 31, 9, 47, 55, 293098))),
                ('comment', ckeditor_uploader.fields.RichTextUploadingField(default=None)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.newspost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
