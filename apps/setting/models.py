from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=244,
        verbose_name="Название сайта",
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo_site"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер",
        blank=True,null=True        
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank=True,null=True    
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank=True,null=True        
    )
    graphic = models.CharField(
        max_length=255,
        verbose_name="График работы",
        blank=True,null=True
    )
    locate_url = models.URLField(
        verbose_name="Ссылка для адресса",
        blank=True,null=True        
    )
    facebook = models.URLField(
        verbose_name="Facebook",
        blank=True,null=True        
    )
    instagram = models.URLField(
        verbose_name="Instagram",
        blank=True,null=True        
    )
    whatsapp = models.URLField(
        verbose_name="Whatsapp",
        blank=True,null=True        
    )
    youtube = models.URLField(
        verbose_name="Youtube",
        blank=True,null=True        
    )
    app = models.URLField(
        verbose_name="Ссылка для приложения",
        blank=True,null=True        
    )
    
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
        
        
class About(models.Model):
    descriptions = models.TextField(
        verbose_name="Первое описание"
    )
    desscriptions2 = models.TextField(
        verbose_name="Второе описание"
    )
    image = models.ImageField(
        upload_to="about_image",
        verbose_name="Фотография"
    )
    experience = models.CharField(
        max_length=255,
        verbose_name="опыт"
    )
    7
    def  __str__(self):
        return f" {self.descriptions} - {self.desscriptions2}"
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        
class History(models.Model):
    years = models.CharField(
        max_length=255,
        verbose_name="Год"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="history_image",
        verbose_name="Фотография"
    )
    
    def __str__(self):
        return f"{self.years} - {self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Наши истории"
        verbose_name_plural = "Наша история"