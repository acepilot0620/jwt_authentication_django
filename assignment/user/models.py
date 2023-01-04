from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampModel
from .user_manager import UserManager

class User(AbstractUser, TimeStampModel):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = "사용자 정보"
        verbose_name_plural = "사용자 정보들"

