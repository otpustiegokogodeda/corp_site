from weasyprint import HTML
from django.template.loader import render_to_string
import tempfile


def generate_invoice_pdf(order, invoice):
    html_string = render_to_string("invoices/invoice_template.html", {"order": order, "invoice": invoice})

    with tempfile.NamedTemporaryFile(delete=True, suffix=".pdf") as output:
        HTML(string=html_string).write_pdf(target=output.name)
        output.seek(0)
        invoice.pdf_file.save(f"invoice_{invoice.id}.pdf", output)