from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "service", "status", "amount", "created_at")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("user__email", "service__title")
    readonly_fields = ("created_at", "updated_at")