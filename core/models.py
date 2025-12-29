from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    """Главная страница"""
    
    hero_title = models.CharField(
        max_length=255,
        default='Добро пожаловать!',
        verbose_name='Заголовок hero-блока'
    )
    hero_subtitle = RichTextField(
        default='',
        blank=True,
        verbose_name='Подзаголовок hero-блока'
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Фото hero-блока'
    )
    
    show_featured_news = models.BooleanField(
        default=True,
        verbose_name='Показывать блок "О компании"'
    )
    featured_section_title = models.CharField(
        max_length=255,
        default='О компании',
        verbose_name='Название блока'
    )
    featured_section_text = RichTextField(
        default='',
        blank=True,
        verbose_name='Текст блока'
    )
    featured_section_button_text = models.CharField(
        max_length=100,
        default='Подробнее',
        verbose_name='Текст кнопки'
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
        FieldPanel('hero_image'),
        FieldPanel('show_featured_news'),
        FieldPanel('featured_section_title'),
        FieldPanel('featured_section_text'),
        FieldPanel('featured_section_button_text'),
    ]
    
    subpage_types = ['core.AboutPage', 'news.NewsIndexPage', 'contacts.ContactsPage']
    parent_page_types = ['wagtailcore.Page']
    
    def get_context(self, request):
        context = super().get_context(request)
        from news.models import NewsPage
        context['news_list'] = NewsPage.objects.filter(live=True).order_by('-first_published_at')[:3]
        return context
    
    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'


class AboutPage(Page):
    """Страница об организации"""
    
    intro_text = RichTextField(
        verbose_name='Вводный текст'
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
    ]
    
    parent_page_types = ['core.HomePage']
    subpage_types = []
    
    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'