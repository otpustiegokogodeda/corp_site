import requests
from django.conf import settings

BITRIX_WEBHOOK_URL = settings.BITRIX_WEBHOOK_URL

def send_to_crm_lead(name, email, phone, service_title, amount):
    url = f"{BITRIX_WEBHOOK_URL}/crm.lead.add.json"
    payload = {
        "fields": {
            "TITLE": f"Заказ услуги: {service_title}",
            "NAME": name,
            "EMAIL": [{"VALUE": email, "VALUE_TYPE": "WORK"}],
            "PHONE": [{"VALUE": phone, "VALUE_TYPE": "WORK"}],
            "COMMENTS": f"Сумма заказа: {amount} ₽"
        }
    }
    response = requests.post(url, json=payload)
    return response.json()

def get_crm_leads():
    url = f"{BITRIX_WEBHOOK_URL}/crm.lead.list.json"
    params = {
        "select": ["ID", "TITLE", "NAME", "EMAIL", "PHONE", "COMMENTS"]
    }
    response = requests.get(url, params=params)
    return response.json()

def update_crm_lead_status(lead_id, status):
    url = f"{BITRIX_WEBHOOK_URL}/crm.lead.update.json"
    payload = {
        "id": lead_id,
        "fields": {"STATUS_ID": status}
    }
    response = requests.post(url, json=payload)
    return response.json()