from .models import PopupNotification

def popup_notifications(request):
    path = request.path
    notifications = PopupNotification.objects.filter(is_active=True)

    active_popups = [
        n for n in notifications if any(page in path for page in n.get_pages_list())
    ]

    return {"popup_notifications": active_popups}