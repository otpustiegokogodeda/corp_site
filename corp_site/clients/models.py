from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class UserRole(models.TextChoices):
    ADMIN = "admin", _("Администратор")
    MANAGER = "manager", _("Менеджер")
    ACCOUNTANT = "accountant", _("Бухгалтер")
    CLIENT = "client", _("Клиент")


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email"), unique=True)
    role = models.CharField(
        _("Роль"),
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CLIENT,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.email