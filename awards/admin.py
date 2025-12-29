from django.contrib import admin
from .models import Award

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'image')
        }),
        ('Параметры', {
            'fields': ('is_published', 'created_at')
        }),
    )
    readonly_fields = ('created_at',)
