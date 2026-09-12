from modeltranslation.translator import register, TranslationOptions
from .models import Book

@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'short_description', 'long_description', 'seo_title', 'seo_description')
