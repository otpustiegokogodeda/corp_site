from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from core.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", TemplateView.as_view(template_name="base.html"), name="home"),
    path("", home, name="home1"),
]