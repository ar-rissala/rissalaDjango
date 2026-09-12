from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username')
