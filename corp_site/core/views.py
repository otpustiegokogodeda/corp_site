from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        full_message = f"От: {name} <{email}>\n\n{message}"
        send_mail(
            subject="Сообщение с контактной формы",
            message=full_message,
            from_email=None,
            recipient_list=["rbarsuk7@gmail.com"],
        )

        messages.success(request, "Спасибо! Мы получили ваше сообщение.")
        return redirect("contact")
    
    return render(request, "contact.html")