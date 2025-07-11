from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255,verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name



class Authors(models.Model):
    auth_name = models.CharField(max_length=255,verbose_name='Имя автора')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    
    def __str__(self):
        return self.auth_name



class Book(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название')
    pages = models.PositiveIntegerField(verbose_name='Страницы')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Категория')
    author = models.ForeignKey(Authors,on_delete=models.CASCADE,verbose_name='Автор')
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='books')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
    
    def __str__(self):
        return self.title