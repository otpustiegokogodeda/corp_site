from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from invoices.models import Invoice
from django.views.decorators.http import require_POST
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm
from .models import EmailConfirmation
from django.contrib import messages
from django.contrib.auth import logout

@login_required
def dashboard_view(request):
    orders = Order.objects.filter(user=request.user).select_related('service').order_by('-created_at')
    invoices = Invoice.objects.filter(order__user=request.user).select_related('order')
    return render(request, 'clients/dashboard.html', {
        'orders': orders,
        'invoices': invoices,
    })

@require_POST
@login_required
def repeat_order_view(request, order_id):
    original = get_object_or_404(Order, id=order_id, user=request.user)
    Order.objects.create(
        user=request.user,
        service=original.service,
        amount=original.amount,
        status='created',
    )
    return redirect('clients:dashboard')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            confirm = EmailConfirmation.objects.create(user=user)

            confirm_url = f"{request.build_absolute_uri('/clients/confirm-email/')}?token={confirm.token}"
            send_mail(
                'Подтверждение регистрации',
                f'Здравствуйте, {user.email}!\n\nПерейдите по ссылке для активации аккаунта:\n{confirm_url}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False
            )

            return render(request, 'clients/check_email.html')
    else:
        form = RegisterForm()
    return render(request, 'clients/register.html', {'form': form})


def confirm_email_view(request):
    token = request.GET.get('token')
    try:
        confirm = EmailConfirmation.objects.get(token=token)
        if not confirm.confirmed:
            confirm.confirmed = True
            confirm.save()
            confirm.user.is_active = True
            confirm.user.save()
            messages.success(request, 'E-mail успешно подтверждён! Теперь вы можете войти.')
            return redirect('login')
        else:
            messages.info(request, 'E-mail уже был подтверждён.')
            return redirect('login')
    except EmailConfirmation.DoesNotExist:
        return render(request, 'clients/invalid_token.html')