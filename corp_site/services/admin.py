from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")