from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'position_order', 'is_published')
    list_editable = ('position_order', 'is_published')
    search_fields = ('full_name', 'position')
    fieldsets = (
        ('Основная информация', {
            'fields': ('full_name', 'position', 'photo')
        }),
        ('Параметры', {
            'fields': ('position_order', 'is_published')
        }),
    )
