from django.contrib import admin
from .models import Service
from core.admin_mixins import RoleBasedAdminMixin

@admin.register(Service)
class ServiceAdmin(RoleBasedAdminMixin, admin.ModelAdmin):
    list_display = ("title", "price", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)

    allowed_roles_view = ["admin", "manager"]
    allowed_roles_add = ["admin", "manager"]
    allowed_roles_change = ["admin", "manager"]
    allowed_roles_delete = ["admin"]