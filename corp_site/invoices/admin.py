from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "is_paid", "issued_at", "paid_at", "pdf_file")
    list_filter = ("is_paid", "issued_at", "paid_at")
    search_fields = ("order__id", "order__user__email")
    readonly_fields = ("issued_at", "paid_at", "pdf_file")