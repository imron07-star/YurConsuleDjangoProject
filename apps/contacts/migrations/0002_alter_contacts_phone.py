# Generated by Django 5.0.4 on 2024-04-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.IntegerField(verbose_name='Телефонный номер'),
        ),
    ]
