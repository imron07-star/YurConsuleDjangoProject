# Generated by Django 4.2 on 2023-04-27 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0011_setting_instagram_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Setting',
        ),
    ]