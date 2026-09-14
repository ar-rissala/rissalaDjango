from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Book(models.Model):
    language = models.CharField(_('language'), max_length=2, choices=[('en', 'English'), ('ar', 'Arabic')], default='en')
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.CharField(_('author'), max_length=255)
    short_description = models.TextField(_('short description'), blank=True)
    long_description = models.TextField(_('long description'), blank=True)
    cover_image = models.ImageField(_('cover image'), upload_to='books/covers/', blank=True, null=True)
    pdf_file = models.FileField(_('PDF file'), upload_to='books/pdfs/', blank=True, null=True)
    external_pdf_url = models.URLField(_('external PDF URL'), blank=True, help_text=_("If stored on R2 directly"))
    category = models.CharField(_('category'), max_length=100, blank=True)
    subcategory = models.CharField(_('subcategory'), max_length=100, blank=True)
    tags = models.CharField(_('tags'), max_length=255, blank=True)
    publication_date = models.DateField(_('publication date'), blank=True, null=True)
    status = models.CharField(_('status'), max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    featured = models.BooleanField(_('featured'), default=False)
    order = models.PositiveIntegerField(_('order'), default=0)
    seo_title = models.CharField(_('SEO title'), max_length=255, blank=True)
    seo_description = models.TextField(_('SEO description'), blank=True)

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
        ordering = ['order', '-publication_date']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        from django.utils import translation
        with translation.override(self.language):
            return reverse('books:detail', kwargs={'slug': self.slug})
