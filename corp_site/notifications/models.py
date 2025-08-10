from django.db import models

class PopupNotification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    show_on_pages = models.CharField(
        max_length=255,
        help_text="Список URL через запятую, где показывать попап"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_pages_list(self):
        return [p.strip() for p in self.show_on_pages.split(",") if p.strip()]