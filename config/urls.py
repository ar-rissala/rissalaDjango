from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from apps.core.sitemaps import StaticViewSitemap, BookSitemap, ContentSitemap, CourseSitemap
import apps.core.views

sitemaps = {
    'static': StaticViewSitemap,
    'books': BookSitemap,
    'content': ContentSitemap,
    'courses': CourseSitemap,
}

from django.views.generic import TemplateView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('llms.txt', TemplateView.as_view(template_name="llms.txt", content_type="text/plain")),
    path('<str:key>.txt', apps.core.views.indexnow_view, name='indexnow'),
]

from django.utils.translation import gettext_lazy as _

urlpatterns += i18n_patterns(
    path(_('auth/'), include('apps.accounts.urls')),
    path(_('books/'), include('apps.books.urls')),
    path(_('content/'), include('apps.content.urls')),
    path(_('courses/'), include('apps.courses.urls')),
    path('', include('apps.core.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
