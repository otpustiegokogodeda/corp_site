from django import forms
from services.models import Service

class LeadForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100)
    last_name = forms.CharField(label="Фамилия", max_length=100)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Телефон", max_length=50)
    service = forms.ModelChoiceField(label="Услуга", queryset=Service.objects.all())