from django.db import models
from django.utils.translation import gettext_lazy as _
from clients.models import CustomUser
from services.models import Service


class OrderStatus(models.TextChoices):
    CREATED = "created", _("Создан")
    PAID = "paid", _("Оплачен")
    PROCESSING = "processing", _("В обработке")
    COMPLETED = "completed", _("Завершён")
    CANCELED = "canceled", _("Отменён")


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Клиент"))
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name=_("Услуга"))
    status = models.CharField(
        _("Статус"),
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.CREATED,
    )
    amount = models.DecimalField(_("Сумма"), max_digits=10, decimal_places=2, blank=True)
    
    created_at = models.DateTimeField(_("Создано"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Обновлено"), auto_now=True)

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заказ #{self.id} от {self.user.email}"

    def save(self, *args, **kwargs):
        if not self.amount:
            self.amount = self.service.price
        super().save(*args, **kwargs)