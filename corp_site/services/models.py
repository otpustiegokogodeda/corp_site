from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    title = models.CharField(_("Название"), max_length=255)
    description = models.TextField(_("Описание"))
    price = models.DecimalField(_("Цена"), max_digits=10, decimal_places=2)
    is_active = models.BooleanField(_("Активна"), default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title