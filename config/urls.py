from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.urls import path, include

# Dynamic admin path from settings
admin_path = getattr(settings, 'ADMIN_PATH', 'control')

urlpatterns = [
    # Admin and Wagtail
    path(f'{admin_path}/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
]

# App-specific URLs
urlpatterns += [
    path('', include('core.urls', namespace='core')),
    path('news/', include('news.urls', namespace='news')),
    path('people/', include('people.urls', namespace='people')),
    path('awards/', include('awards.urls', namespace='awards')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
]

# Wagtail (last, catch-all)
urlpatterns += [
    path('', include(wagtail_urls)),
]

# Media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
