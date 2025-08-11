from django.shortcuts import render, redirect, get_object_or_404
from services.models import Service
from .models import Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def create_order_view(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            service=service,
            amount=service.price
        )
        messages.success(request, f"Заказ на услугу «{service.title}» успешно оформлен!")
        return redirect('clients:dashboard')

    return render(request, 'orders/confirm_order.html', {'service': service}) 

@login_required
def orders_list_view(request):
    user = request.user
    orders = Order.objects.all()

    if user.role == 'manager':
        orders = orders.filter(manager=user)

    return render(request, "orders/orders_list.html", {"orders": orders})