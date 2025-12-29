from wagtail import hooks
from wagtail.admin.menu import Menu, MenuItem
from django.urls import reverse
from wagtail.admin.search import SearchArea
from news.models import NewsPage
from people.models import Person
from awards.models import Award


@hooks.register('register_admin_menu_item')
def register_news_menu_item():
    return MenuItem(
        'Новости',
        reverse('wagtailadmin_explore_root'),
        classname='icon icon-doc-full-inverse',
        order=100
    )


@hooks.register('register_admin_search_area')
def register_search_areas():
    return SearchArea(
        'Новости',
        reverse('wagtailadmin_explore', args=[2]),
        classname='icon icon-doc-full-inverse',
        order=100,
    )
