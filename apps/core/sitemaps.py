from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.books.models import Book
from apps.content.models import Content
from apps.courses.models import Course

class StaticViewSitemap(Sitemap):
    i18n = True
    alternates = True
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return [
            'core:home', 'core:about', 'core:legal', 'core:privacy', 'core:terms',
            'accounts:login', 'accounts:register',
            'books:list', 'courses:list', 'content:news_list'
        ]

    def location(self, item):
        return reverse(item)

class BookSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Book.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.publication_date

class ContentSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Content.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.published_at

class CourseSitemap(Sitemap):
    i18n = True
    alternates = True
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Course.objects.filter(status='published')
