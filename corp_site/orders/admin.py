from django.contrib import admin
from .models import Order
from core.admin_mixins import RoleBasedAdminMixin

@admin.register(Order)
class OrderAdmin(RoleBasedAdminMixin, admin.ModelAdmin):
    list_display = ("id", "user", "service", "status", "amount", "created_at")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("user__email", "service__title")
    readonly_fields = ("created_at", "updated_at")

    allowed_roles_view = ["admin", "manager"]
    allowed_roles_add = ["admin", "manager"]
    allowed_roles_change = ["admin", "manager"]
    allowed_roles_delete = ["admin"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if getattr(request.user, "role", None) == "manager":
            return qs.filter(user=request.user)
        return qs.none()
    
    def has_change_permission(self, request, obj=None):
        if obj and getattr(request.user, "role", None) == "manager":
            return obj.user == request.user
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and getattr(request.user, "role", None) == "manager":
            return obj.user == request.user
        return super().has_delete_permission(request, obj)