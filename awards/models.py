from django.db import models
from wagtail.search import index


class Award(models.Model):
    """Модель награды/благодарности"""
    
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    
    image = models.ImageField(
        upload_to='awards/',
        verbose_name='Изображение'
    )
    
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )
    
    search_fields = [
        index.SearchField('title', partial_match=True),
        index.SearchField('description'),
    ]
    
    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title
