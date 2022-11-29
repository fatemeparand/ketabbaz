from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    list_display = ('username', 'email')

