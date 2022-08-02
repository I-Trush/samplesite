from django.db import models


# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')   # связь внешний ключ, теперь эта модель вторична, а модель Rubric первична//on_delete=models.PROTECT запрет каскадного удаления

    class Meta:                             # класс, атрибуты которого зададут параметры самой додели
        verbose_name_plural = 'Объявления'  # название модели во множественном числе
        verbose_name = 'Объявление'         # название модели в единственном числе
        ordering = ['-published']           # последовательность полей, для которых будет выполняться сортировка по умолчанию


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
