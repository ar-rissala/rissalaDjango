from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'courses'

urlpatterns = [
    path(_('parcours/'), views.CourseListView.as_view(), name='list'),
    path(_('sciences-islamiques/'), views.CourseListView.as_view(), name='list_sciences'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='detail'),
]
