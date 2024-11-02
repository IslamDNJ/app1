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
# Для ImageField Нужна библеотека Pillow [pip install Pillow]

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = "category"
        verbose_name ='Категорию'
        verbose_name_plural ='Категории'

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(max_length=10000,blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00,max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00,max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = "product"
        verbose_name ='Продукт'
        verbose_name_plural ='Продукты'

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price* self.discount/100, 2)
        
        return self.price