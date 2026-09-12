from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'content'

urlpatterns = [
    path(_('actualites/'), views.NewsListView.as_view(), name='news_list'),
    
    path(_('langue-arabe/'), views.ContentListView.as_view(
        content_type_filter='arabic',
        page_title=_("Langue Arabe"),
        page_description=_("Ressources et articles dédiés à l'étude de la langue arabe.")
    ), name='arabic_list'),
    
    path(_('finance-islamique/'), views.ContentListView.as_view(
        content_type_filter='finance',
        page_title=_("Finance Islamique"),
        page_description=_("Articles et analyses sur les principes de la finance islamique.")
    ), name='finance_list'),
    
    path(_('sciences-islamiques/'), views.ContentListView.as_view(
        content_type_filter='science',
        page_title=_("Sciences Islamiques"),
        page_description=_("Ressources éducatives sur les fondements de la religion et la spiritualité.")
    ), name='science_list'),
    
    path('<slug:slug>/', views.ContentDetailView.as_view(), name='detail'),
]
