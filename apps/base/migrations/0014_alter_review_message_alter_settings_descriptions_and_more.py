# Generated by Django 5.0.4 on 2024-04-26 22:13

import ckeditor.fields
import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_rename_logate_settings_locate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='message',
            field=ckeditor.fields.RichTextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='descriptions',
            field=ckeditor.fields.RichTextField(verbose_name='Описание сайта'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/', verbose_name='Фото для сайта'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image1',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image1/', verbose_name='2 Фото для сайта'),
        ),
    ]
