from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language', 'status', 'publication_date', 'featured', 'order')
    list_filter = ('language', 'status', 'featured', 'category')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publication_date'
    fieldsets = (
        ('Livre et Langue (Requis)', {
            'fields': ('language', 'title', 'slug', 'author', 'pdf_file', 'external_pdf_url')
        }),
        ('Détails', {
            'fields': ('short_description', 'long_description', 'cover_image', 'category', 'subcategory', 'tags')
        }),
        ('Publication & SEO', {
            'fields': ('status', 'featured', 'order', 'publication_date', 'seo_title', 'seo_description')
        }),
    )
