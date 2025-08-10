from django.contrib import admin
from .models import PopupNotification

@admin.register(PopupNotification)
class PopupNotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "message", "show_on_pages")