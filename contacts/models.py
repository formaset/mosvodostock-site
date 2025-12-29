from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class ContactsPage(Page):
    """Страница контактов"""
    
    intro = RichTextField(
        verbose_name='Краткое описание',
        blank=True
    )
    
    full_name = models.CharField(
        max_length=255,
        verbose_name='Полное наименование организации',
        default=''
    )
    
    short_name = models.CharField(
        max_length=255,
        verbose_name='Сокращённое наименование',
        default=''
    )
    
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
        default=''
    )
    
    email = models.EmailField(
        verbose_name='Email',
        default=''
    )
    
    legal_address = models.TextField(
        verbose_name='Юридический адрес',
        default=''
    )
    
    actual_address = models.TextField(
        verbose_name='Фактический адрес',
        default=''
    )
    
    working_hours = models.CharField(
        max_length=255,
        verbose_name='График работы',
        default='ПН-ЧТ 08:00-17:00, ПТ 08:00-16:00, перерыв 12:00-13:00'
    )
    
    yandex_maps_embed = models.TextField(
        verbose_name='Код внедрения Яндекс.Карты',
        help_text='Вставьте iframe код для эмбеда карты',
        blank=True
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('full_name'),
        FieldPanel('short_name'),
        FieldPanel('phone'),
        FieldPanel('email'),
        FieldPanel('legal_address'),
        FieldPanel('actual_address'),
        FieldPanel('working_hours'),
        FieldPanel('yandex_maps_embed'),
    ]
    
    parent_page_types = ['core.HomePage']
    subpage_types = []
    
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
