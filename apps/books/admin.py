from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Book

@admin.register(Book)
class BookAdmin(TranslationAdmin):
    list_display = ('title', 'author', 'status', 'publication_date', 'featured', 'order')
    list_filter = ('status', 'featured', 'category')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug_fr': ('title_fr',), 'slug_en': ('title_en',), 'slug_ar': ('title_ar',)}
    date_hierarchy = 'publication_date'
