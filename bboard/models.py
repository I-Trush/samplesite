from django.db import models


# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    class Meta:                             #класс, атрибуты которого зададут параметры самой додели
        verbose_name_plural = 'Объявления'  #название модели во множественном числе
        verbose_name = 'Объявление'         #название модели в единственном числе
        ordering = ['-published']           #последовательность полей, для которых будет выполняться сортировка по умолчанию

