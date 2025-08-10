from django.urls import path
from .views import create_order_view, orders_list_view

app_name = 'orders'

urlpatterns = [
    path('', orders_list_view, name='orders_list'),
    path('create/<int:service_id>/', create_order_view, name='create_order'),
]