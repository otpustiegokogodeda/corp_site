from django.db import models
from django.utils.translation import gettext_lazy as _
from orders.models import Order


class Invoice(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name=_("Заказ"))
    pdf_file = models.FileField(_("PDF файл"), upload_to="invoices/")
    is_paid = models.BooleanField(_("Оплачен"), default=False)
    issued_at = models.DateTimeField(_("Дата выставления"), auto_now_add=True)
    paid_at = models.DateTimeField(_("Дата оплаты"), null=True, blank=True)

    class Meta:
        verbose_name = _("Счёт")
        verbose_name_plural = _("Счета")
        ordering = ["-issued_at"]

    def __str__(self):
        return f"Счёт #{self.id} для заказа #{self.order.id}"