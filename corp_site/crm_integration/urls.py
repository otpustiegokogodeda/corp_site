from django.urls import path
from .views import crm_clients_view

app_name = 'crm_integration'

urlpatterns = [
    
    path("clients/", crm_clients_view, name="crm_clients"),
]