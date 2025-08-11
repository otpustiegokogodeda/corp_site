from django.contrib import admin
from .models import Banner
from core.admin_mixins import RoleBasedAdminMixin

@admin.register(Banner)
class BannerAdmin(RoleBasedAdminMixin, admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "is_active")
    list_filter = ("is_active", "start_date", "end_date")
    search_fields = ("title",)

    allowed_roles_view = ["admin", "manager"]
    allowed_roles_add = ["admin", "manager"]
    allowed_roles_change = ["admin", "manager"]
    allowed_roles_delete = ["admin"]