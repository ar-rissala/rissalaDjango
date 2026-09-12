from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Content

@admin.register(Content)
class ContentAdmin(TranslationAdmin):
    list_display = ('title', 'content_type', 'status', 'is_featured', 'published_at')
    list_filter = ('content_type', 'status', 'is_featured')
    search_fields = ('title', 'author', 'content')
    prepopulated_fields = {'slug_fr': ('title_fr',), 'slug_en': ('title_en',), 'slug_ar': ('title_ar',)}
    date_hierarchy = 'published_at'
