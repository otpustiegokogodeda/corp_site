from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order
from .utils import generate_invoice
from crm_integration.bitrix import send_to_crm_lead

@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        pdf_url = generate_invoice(instance)
        full_pdf_url = f"{settings.SITE_URL}{pdf_url}"

        send_mail(
            subject='Новый заказ',
            message=f'Ваш заказ #{instance.id} создан. Счёт: {full_pdf_url}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.user.email],
            fail_silently=False,
        )

@receiver(post_save, sender=Order)
def order_to_crm(sender, instance, created, **kwargs):
    if created:
        send_to_crm_lead(
            name=instance.user.name,
            email=instance.user.email,
            phone=getattr(instance.user, 'phone', ''),
            service_title=instance.service.title,
            amount=instance.amount
        )