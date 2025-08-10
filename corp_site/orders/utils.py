import weasyprint
from django.template.loader import render_to_string
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def generate_invoice(order):
    html = render_to_string('orders/invoice.html', {'order': order})

    pdf_file = weasyprint.HTML(string=html, base_url=settings.STATIC_ROOT).write_pdf()

    fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'invoices'))
    if not os.path.exists(fs.location):
        os.makedirs(fs.location)

    filename = f'order_{order.id}.pdf'
    with fs.open(filename, 'wb') as f:
        f.write(pdf_file)

    return f'{settings.MEDIA_URL}invoices/{filename}'