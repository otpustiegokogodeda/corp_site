from django.urls import path
from .views import crm_clients_view, create_lead_view

app_name = 'crm_integration'

urlpatterns = [
    
    path("clients/", crm_clients_view, name="crm_clients"),
    path("create_lead/", create_lead_view, name="create_lead"),
]