from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('a-propos/', views.AboutView.as_view(), name='about'),
    path('mentions-legales/', views.LegalView.as_view(), name='legal'),
    path('politique-de-confidentialite/', views.PrivacyView.as_view(), name='privacy'),
    path('conditions-generales/', views.TermsView.as_view(), name='terms'),
]
