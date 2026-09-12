from modeltranslation.translator import register, TranslationOptions
from .models import Content

@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'excerpt', 'content', 'seo_title', 'seo_description')
