from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='Слагифицированное имя')

    class Meta:
        ordering = ['id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='media/', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.FloatField(blank=True, verbose_name='Цена')
    slug = models.SlugField(max_length=200, verbose_name='Слагифицированное имя')

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_detail',
                       args=[self.category.slug, self.id])


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    author = models.CharField(max_length=200, verbose_name='Автор')
    text = models.TextField(blank=True, verbose_name='Отзыв')
    rate = models.PositiveIntegerField(default=False, verbose_name='Оценка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
