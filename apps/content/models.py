from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid

class Content(models.Model):
    CONTENT_TYPES = [
        ('news', 'News'),
        ('arabic', 'Arabic Language'),
        ('finance', 'Islamic Finance'),
        ('science', 'Islamic Sciences'),
    ]

    language = models.CharField(_('language'), max_length=2, choices=[('en', 'English'), ('ar', 'Arabic')], default='en')
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content_type = models.CharField(_('content type'), max_length=20, choices=CONTENT_TYPES)
    excerpt = models.TextField(_('excerpt'), blank=True)
    content = models.TextField(_('content'))
    cover_image = models.ImageField(_('cover image'), upload_to='content/covers/', blank=True, null=True)
    author = models.CharField(_('author'), max_length=255, blank=True)
    tags = models.CharField(_('tags'), max_length=255, blank=True)
    status = models.CharField(_('status'), max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    is_featured = models.BooleanField(_('featured'), default=False)
    published_at = models.DateTimeField(_('published at'), blank=True, null=True)
    seo_title = models.CharField(_('SEO title'), max_length=255, blank=True)
    seo_description = models.TextField(_('SEO description'), blank=True)

    class Meta:
        verbose_name = _('content')
        verbose_name_plural = _('contents')
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['content_type']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        from django.utils import translation
        with translation.override(self.language):
            return reverse('content:detail', kwargs={'slug': self.slug})
