from django.contrib import admin
from .models import Invoice
from core.admin_mixins import RoleBasedAdminMixin

@admin.register(Invoice)
class InvoiceAdmin(RoleBasedAdminMixin, admin.ModelAdmin):
    list_display = ("id", "order", "is_paid", "issued_at", "paid_at", "pdf_file")
    list_filter = ("is_paid", "issued_at", "paid_at")
    search_fields = ("order__id", "order__user__email")
    readonly_fields = ("issued_at", "pdf_file")

    allowed_roles_view = ["admin", "accountant"]
    allowed_roles_add = ["admin"]
    allowed_roles_change = ["admin", "accountant"]
    allowed_roles_delete = ["admin"]