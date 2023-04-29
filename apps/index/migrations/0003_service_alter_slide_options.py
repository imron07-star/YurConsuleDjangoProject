# Generated by Django 4.2 on 2023-04-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='servie_image', verbose_name='Наши услуги')),
                ('name', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('descriptions', models.TextField(verbose_name='Описание про нащших услуг')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуга',
            },
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': 'Слайды', 'verbose_name_plural': 'Слайды'},
        ),
    ]
