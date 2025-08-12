from django.shortcuts import render
from .bitrix import get_crm_leads

def crm_clients_view(request):
    leads = get_crm_leads()
    return render(
        request,
        "crm_integration/clients.html",
        {"leads": leads}
    )