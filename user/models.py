from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as __
from django.contrib.auth import get_user_model

from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(__("Email adress"), unique=True)
    is_staff = models.BooleanField(__("is staff"), default=False)
    is_active = models.BooleanField(__("is active"), default=True)
    date_joined = models.DateTimeField(__("date joined"), auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = __('user')
        app_label = 'user'

User = get_user_model()