from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from wagtail.models import Page
from core.models import HomePage, AboutPage
from news.models import NewsIndexPage, NewsPage
from contacts.models import ContactsPage
from people.models import Person
from awards.models import Award
from wagtail.images.models import Image
from django.core.files.base import ContentFile
import io
from PIL import Image as PILImage


class Command(BaseCommand):
    help = 'Популяти расодом с начинающими данными'

    def handle(self, *args, **options):
        # Отрываются правы доступа для ОПАЦІОН ЕДИТОРОВ
        self.setup_permissions()
        
        # Создаэм главные страницы
        self.create_pages()
        
        # Создаэм тестовые данные
        self.create_test_data()
        
        self.stdout.write(self.style.SUCCESS('Финальная бутстрап конфигурация сайта'))

    def setup_permissions(self):
        """Настройка групп доступа"""
        group, created = Group.objects.get_or_create(name='Новости Редактор')
        if created:
            self.stdout.write(f'Группа {group.name} создана')

    def create_pages(self):
        """Создание основных страниц"""
        root = Page.get_root_nodes().first()
        
        # Проверим наличие главной
        if not HomePage.objects.exists():
            home = HomePage.objects.create(
                title='МосводостокСтройТрест',
                slug='home'
            )
            root.add_child(instance=home)
            home.save_revision().publish()
            self.stdout.write(f'Главная страница создана')
        else:
            home = HomePage.objects.first()
        
        # Об организации
        if not AboutPage.objects.exists():
            about = AboutPage.objects.create(
                title='Об организации',
                slug='about',
                intro_text='АНО По развитию городской среды МосводостокСтройТрест — надежный партнер в благоустройстве города.'
            )
            home.add_child(instance=about)
            about.save_revision().publish()
            self.stdout.write(f'Страница Об организации создана')
        
        # Новости
        if not NewsIndexPage.objects.exists():
            news = NewsIndexPage.objects.create(
                title='Новости',
                slug='news'
            )
            home.add_child(instance=news)
            news.save_revision().publish()
            self.stdout.write(f'Финда новостей создана')
        
        # Контакты
        if not ContactsPage.objects.exists():
            contacts = ContactsPage.objects.create(
                title='Контакты',
                slug='contacts',
                full_name='АНО По развитию городской среды МосводостокСтройТрест',
                short_name='МСТ',
                phone='+7 (495) 123-45-67',
                email='info@mosvodostock.ru',
                legal_address='Москва, стр. 123'
            )
            home.add_child(instance=contacts)
            contacts.save_revision().publish()
            self.stdout.write(f'Страница Контактов создана')

    def create_test_data(self):
        """Создание тестовых данных"""
        # Создаем тестовые данные для руководства
        if not Person.objects.exists():
            Person.objects.create(
                full_name='Образец ФВ',
                position='Образец работы',
                position_order=1
            )
            self.stdout.write('Образцовые роли созданы')

        # Содаем самшую награду
        if not Award.objects.exists():
            Award.objects.create(
                title='Лучших
',
                description='Найвысшие денежные призы для всех сотрудников'
            )
            self.stdout.write('Награды созданы')
