from django.urls import path
from .views import banner_list

app_name = "banners"

urlpatterns = [
    path("", banner_list, name="banner_list"),
]