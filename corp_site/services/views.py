from django.shortcuts import render
from .models import Service

def service_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, "services/list.html", {"services": services})