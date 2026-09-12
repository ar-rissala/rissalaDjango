from django import template
from django.urls import resolve, reverse
from django.utils import translation
import logging

logger = logging.getLogger(__name__)
register = template.Library()

@register.simple_tag(takes_context=True)
def translated_url(context, lang_code):
    request = context.get('request')
    if not request:
        return ''
    
    url_name = request.resolver_match.url_name
    namespace = request.resolver_match.namespace
    view_name = f"{namespace}:{url_name}" if namespace else url_name
    kwargs = request.resolver_match.kwargs.copy()
    
    if 'slug' in kwargs:
        obj = context.get('object') or context.get('book') or context.get('content_obj') or context.get('course')
        if obj:
            # Try to get the translated slug
            translated_slug = getattr(obj, f'slug_{lang_code}', None)
            if translated_slug:
                kwargs['slug'] = translated_slug
            elif hasattr(obj, 'slug'):
                kwargs['slug'] = obj.slug
                
    with translation.override(lang_code):
        try:
            return reverse(view_name, args=request.resolver_match.args, kwargs=kwargs)
        except Exception as e:
            logger.error(f"Error reversing {view_name} for lang {lang_code}: {e}")
            return request.get_full_path()
