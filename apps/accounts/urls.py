from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('connexion/', views.LoginView.as_view(), name='login'),
    path('inscription/', views.RegisterView.as_view(), name='register'),
    path('deconnexion/', auth_views.LogoutView.as_view(), name='logout'),
    path('mon-espace/', views.DashboardView.as_view(), name='dashboard'),
]
