from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'language', 'status', 'is_featured', 'published_at')
    list_filter = ('content_type', 'language', 'status', 'is_featured')
    search_fields = ('title', 'author', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    fieldsets = (
        ('Contenu et Langue (Requis)', {
            'fields': ('language', 'content_type', 'title', 'slug', 'author')
        }),
        ('Détails du Contenu', {
            'fields': ('excerpt', 'content', 'cover_image', 'tags')
        }),
        ('Publication & SEO', {
            'fields': ('status', 'is_featured', 'published_at', 'seo_title', 'seo_description')
        }),
    )
