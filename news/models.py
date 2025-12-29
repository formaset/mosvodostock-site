from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import StreamField, RichTextField
from wagtail.blocks import (
    CharBlock, RichTextBlock, StreamBlock, StructBlock,
    TextBlock, ImageChooserBlock, VideoChooserBlock
)
from wagtail.images.blocks import ImageChooserBlock as WagtailImageChooserBlock
from wagtail.media.blocks import VideoChooserBlock as WagtailVideoChooserBlock
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from django.templatetags.static import static


class NewsIndexPage(Page):
    """Ну джетым"""
    
    intro = RichTextField(
        blank=True,
        default='',
        verbose_name='Вводный текст'
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    
    subpage_types = ['news.NewsPage']
    parent_page_types = ['core.HomePage']
    
    def get_context(self, request):
        context = super().get_context(request)
        from django.core.paginator import Paginator
        
        news_list = NewsPage.objects.child_of(self).live().order_by('-first_published_at')
        
        paginator = Paginator(news_list, 10)
        page_num = request.GET.get('page', 1)
        
        try:
            page_obj = paginator.page(page_num)
        except:
            page_obj = paginator.page(1)
        
        context['news_list'] = page_obj.object_list
        context['page_obj'] = page_obj
        return context
    
    class Meta:
        verbose_name = 'Новости'


class QuoteBlock(StructBlock):
    """Оформленная цитата"""
    text = RichTextBlock(label='Текст цитаты')
    author = CharBlock(required=False, label='Автор')

    class Meta:
        template = 'news/blocks/quote_block.html'
        icon = 'openquote'
        label = 'Цитата'


class CalloutBlock(StructBlock):
    """Примечание/выделение"""
    text = RichTextBlock(label='Текст')
    
    class Meta:
        template = 'news/blocks/callout_block.html'
        icon = 'info'
        label = 'Примечание'


class StatisticBlock(StructBlock):
    """Ключевые цифры"""
    number = CharBlock(label='Число')
    label = CharBlock(label='Описание')
    
    class Meta:
        template = 'news/blocks/statistic_block.html'
        icon = 'order'
        label = 'Ключевые цифры'


class GalleryBlock(StructBlock):
    """Галерея изображений"""
    title = CharBlock(required=False, label='Название')
    images = StreamField([
        ('image', WagtailImageChooserBlock())
    ], label='Изображения')
    
    class Meta:
        template = 'news/blocks/gallery_block.html'
        icon = 'image'
        label = 'Галерея'


class SeparatorBlock(StructBlock):
    """Разделитель"""
    
    class Meta:
        template = 'news/blocks/separator_block.html'
        icon = 'minus'
        label = 'Разделитель'


class NewsStreamBlock(StreamBlock):
    """Поток блоков для новостей"""
    heading = CharBlock(icon='title', label='Заголовк')
    paragraph = RichTextBlock(icon='pilcrow', label='Параграф')
    image = WagtailImageChooserBlock(icon='image', label='Изображение')
    video = DocumentChooserBlock(icon='media', label='Видео')
    quote = QuoteBlock(label='Цитата')
    callout = CalloutBlock(label='Примечание')
    statistic = StatisticBlock(label='Статистика')
    gallery = GalleryBlock(label='Галерея')
    separator = SeparatorBlock(label='Разделитель')


class NewsPage(Page):
    """Новость"""
    
    lead = RichTextField(
        verbose_name='Лид (краткое описание)',
        max_length=500
    )
    
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name='Обложка',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    body = StreamField(
        NewsStreamBlock(),
        verbose_name='Основное содержание',
        blank=True
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('lead'),
        FieldPanel('cover_image'),
        FieldPanel('body'),
    ]
    
    parent_page_types = ['news.NewsIndexPage']
    subpage_types = []
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
