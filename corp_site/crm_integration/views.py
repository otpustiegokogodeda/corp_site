from django.shortcuts import render, redirect
from .bitrix import get_crm_leads, send_to_crm_lead
from .forms import LeadForm

def crm_clients_view(request):
    leads = get_crm_leads()
    return render(
        request,
        "crm_integration/clients.html",
        {"leads": leads}
    )
def create_lead_view(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_to_crm_lead(
                name=data["name"],
                email=data["email"],
                phone=data["phone"],
                service_title=data["service"].title,
                amount=data["service"].price
            )
            return redirect("crm_integration:crm_clients")
    else:
        form = LeadForm()

    return render(request, "crm_integration/create_lead.html", {"form": form})