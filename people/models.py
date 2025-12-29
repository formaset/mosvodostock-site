from django.db import models


class Person(models.Model):
    """Модель руководителя"""
    
    full_name = models.CharField(
        max_length=255,
        verbose_name='Полное имя'
    )
    
    position = models.CharField(
        max_length=255,
        verbose_name='Должность'
    )
    
    photo = models.ImageField(
        upload_to='people/',
        null=True,
        blank=True,
        verbose_name='Фото'
    )
    
    position_order = models.IntegerField(
        default=0,
        verbose_name='Порядок сортировки'
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
    
    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководство'
        ordering = ('position_order',)
    
    def __str__(self):
        return f'{self.full_name} ({self.position})'
