# Generated by Django 4.1.7 on 2023-03-22 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0009_rename_news_newspost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newspost',
            options={'verbose_name': '3. NewsPost'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': '2.Subcategory'},
        ),
    ]
