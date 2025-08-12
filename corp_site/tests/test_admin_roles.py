import pytest
from django.urls import reverse
from notifications.models import PopupNotification

@pytest.mark.django_db
def test_popup_notification_visibility(client):
    PopupNotification.objects.create(
        title="Test popup",
        message="Hello",
        show_on_pages="/",
        is_active=True
    )
    # Должен показываться
    resp = client.get("/")
    assert b"Test popup" in resp.content

    # Не должен показываться
    resp = client.get("/contacts")
    assert b"Test popup" not in resp.content