from django.db import models

# Create your models here.

# Поле ID создается автоматически в фале app/settings.py > DEFAULT_AUTO_FIELD
# SlugField - Хранит фрагменты URL-адресов       // varchar
# CharField - Для строк небольшого размера       // varchar
# unique - уникальность
# blank - пустое значение
# null - нулевое значение
# verbose_name - изменяет название в папке
# verbose_name_plural - изменяет название самой папки

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slur = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = "category"
        verbose_name ='Категорию'
        verbose_name_plural ='Категории'
