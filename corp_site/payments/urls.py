from django.urls import path
from .views import create_checkout_session, payment_success, payment_cancel, stripe_webhook

urlpatterns = [
    path('checkout/<int:order_id>/', create_checkout_session, name='checkout'),
    path('payment-success/', payment_success, name='payment_success'),
    path('payment-cancel/', payment_cancel, name='payment_cancel'),
    path('stripe-webhook/', stripe_webhook, name='stripe_webhook'),
]