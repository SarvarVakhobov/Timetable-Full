from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as __

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        (__("Permissions"), {
            "fields": (
                "is_superuser", "is_staff", "is_active",
            )
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": (
                "wide",
            ),
            "fields": (
                'email', 'password1', 'password2', 'is_staff', 'is_active',
            ),
        }),
    )

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    search_fields = ("email", "is_staff", "is_active",)
    ordering = ("email",)

admin.site.register(CustomUser)