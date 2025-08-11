from django.contrib import admin
from .models import PopupNotification
from core.admin_mixins import RoleBasedAdminMixin

@admin.register(PopupNotification)
class PopupNotificationAdmin(RoleBasedAdminMixin, admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)

    allowed_roles_view = ["admin", "manager"]
    allowed_roles_add = ["admin", "manager"]
    allowed_roles_change = ["admin", "manager"]
    allowed_roles_delete = ["admin"]