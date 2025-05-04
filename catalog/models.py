from django.db import models

# Create your models here.


class Category(models.Model):
    """ Класс для представления категории"""
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(null=True, blank=True, verbose_name='описание')

    def __str__(self):
        return f"Категория: {self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        # db_table = ''


class Product(models.Model):
    """ Класс для представления продукта"""
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/',
                              verbose_name='изображение',
                              null=True,
                              blank=True,
                              default='photos/default_tool.jpg',
                              help_text='Загрузите изображение продукта')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='products')
    price = models.FloatField(verbose_name='цена в руб.')
    created_at = models.DateTimeField(auto_now_add=True,
                                      null=True,
                                      blank=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      null=True,
                                      blank=True)

    def __str__(self):
        return f"{self.name}: {self.price}руб."

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['price']
        # db_table = ''
