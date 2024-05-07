from django.db import models
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to = "logo_image/",
        verbose_name="Логотип"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    instagram = models.URLField(
        verbose_name="Instagram url",
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name="facebook url",
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name="youtube url",
        blank=True, null=True
    )
    whatsapp = models.URLField(
        verbose_name="whatsapp url",
        blank=True, null=True
    )
    def __str__(self):
        return f"{self.title} {self.descriptions}"
    
    class Meta:
        verbose_name_plural = "Настройки"

class Slide(models.Model):
    title = models.TextField(
        verbose_name="Описание слайда"
    )
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"


class SlideImage1(models.Model):
    slide = models.ForeignKey(Slide, related_name='about_doing1', on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="slide_image/",
        verbose_name="Фотография для первого слайда"
    )
    class Meta:
        verbose_name_plural = "Фотографии  для первого столбца"
        
class SlideImage2(models.Model):
    slide = models.ForeignKey(Slide, related_name='about_doing2', on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="slide_image/",
        verbose_name="Фотография для первого слайда"
    )

    class Meta:
        verbose_name_plural = "Фотографии для второго столбца"  
        
class Numbers(models.Model):
    client = models.CharField(
        max_length=255,
        verbose_name="Довольные клиенты"
    )
    team = models.CharField(
        max_length=255,
        verbose_name="Опытные юристы и адвокаты"
    )
    experience = models.CharField(
        max_length=255,
        verbose_name="Многолетний опыт"
    )
    critical = models.CharField(
        max_length=255,
        verbose_name="Критические случаи успешно решены"
    )
    review = models.CharField(
        max_length=255,
        verbose_name="Положительных отзывов"
    )
    def __str__(self):
        return f"{self.client} - {self.team} - {self.review} - {self.critical} - {self.experience}"
    
    class Meta:
        verbose_name_plural = "Мы в числах"

class About(models.Model):
    descriptions = models.TextField(
        verbose_name="Первое описание"
    )
    descriptions2 = RichTextField(
        verbose_name="Второе описание"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = 100,
        upload_to="about_image/",
        verbose_name="Фотография"
    )
    def __str__(self):
        return self.descriptions
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'