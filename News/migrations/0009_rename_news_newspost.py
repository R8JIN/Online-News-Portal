# Generated by Django 4.1.7 on 2023-03-22 12:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('News', '0008_alter_category_options_alter_subcategory_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='news',
            new_name='NewsPost',
        ),
    ]
