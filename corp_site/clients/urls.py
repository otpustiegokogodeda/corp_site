from django.urls import path
from .views import dashboard_view, repeat_order_view, register_view, confirm_email_view


app_name = 'clients'

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('repeat/<int:order_id>/', repeat_order_view, name='repeat_order'),
    path('register/', register_view, name='register'),
    path('confirm-email/', confirm_email_view, name='confirm_email'),
]