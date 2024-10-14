from django.db import models

# Create your models here.

# Поле ID создается автоматически в фале app/settings.py > DEFAULT_AUTO_FIELD
# SlugField - Хранит фрагменты URL-адресов       // varchar
# CharField - Для строк небольшого размера       // varchar
# unique - уникальность
# blank - пустое значение
# null - нулевое значение


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True,)
    slur = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = "category"
