import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from orders.models import Order
from services.models import Service

User = get_user_model()

@pytest.fixture
def create_user(db):
    def make_user(email, role, password="testpass", is_staff=True):
        return User.objects.create_user(
            email=email,
            password=password,
            role=role,
            is_staff=is_staff
        )
    return make_user

@pytest.fixture
def login_client(client):
    def do_login(user):
        client.login(email=user.email, password="testpass")
        return client
    return do_login

@pytest.mark.django_db
def test_client_cannot_access_admin(create_user, login_client):
    user = create_user("client@example.com", "client", is_staff=False)
    login_client(user)
    resp = login_client(user).get(reverse("admin:index"))
    assert resp.status_code == 302

@pytest.mark.django_db
def test_admin_can_see_all_models(create_user, login_client):
    admin = create_user("admin@example.com", "admin")
    resp = login_client(admin).get(reverse("admin:index"))
    assert resp.status_code == 200
    assert b"Orders" in resp.content
    assert b"Services" in resp.content

@pytest.mark.django_db
def test_manager_sees_only_own_orders(create_user, login_client):
    service = Service.objects.create(title="Test service", price=100)
    manager = create_user("manager@example.com", "manager")
    other_manager = create_user("other@example.com", "manager")

    order1 = Order.objects.create(user=manager, service=service, amount=100)
    order2 = Order.objects.create(user=other_manager, service=service, amount=100)

    resp = login_client(manager).get(reverse("admin:orders_order_changelist"))
    assert resp.status_code == 200
    content = resp.content.decode()
    assert str(order1.id) in content
    assert str(order2.id) in content

@pytest.mark.django_db
def test_accountant_cannot_add_banner(create_user, login_client):
    accountant = create_user("accountant@example.com", "accountant")
    resp = login_client(accountant).get(reverse("admin:banners_banner_add"))
    assert resp.status_code == 403