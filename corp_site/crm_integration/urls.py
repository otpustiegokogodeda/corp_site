from django.urls import path
from .views import crm_clients_view

urlpatterns = [
    
    path("clients/", crm_clients_view, name="crm_clients"),
]