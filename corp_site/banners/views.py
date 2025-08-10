from datetime import datetime
from django.shortcuts import render
from .models import Banner

def banner_list(request):
    banners = Banner.objects.filter(
        is_active=True,
        start_date__lte=datetime.now(),
        end_date__gte=datetime.now()
    )
    return render(request, "banners/banner_list.html", {"banners": banners})