from django.contrib import admin
from django.urls import path, include
from core.views import home, contact_view
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("contact/", contact_view, name="contact"),
    path('clients/', include('clients.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='clients/login.html'), name='login'),
    path('orders/', include('orders.urls')),
    path("crm/", include("crm_integration.urls")),
    path("banners/", include("banners.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)