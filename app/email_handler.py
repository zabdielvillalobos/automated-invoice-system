import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from flask import render_template
from .models import Invoice

def send_invoice_email(invoice: Invoice):
    sender_email = "youremail@example.com"
    receiver_email = invoice.client_email
    subject = f"Invoice #{invoice.id} for {invoice.service_description}"

    # Email Body
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    body = render_template('invoice_email.html', invoice=invoice)
    msg.attach(MIMEText(body, 'html'))

    # Attach PDF (In a real implementation, you'd generate a PDF and attach it)
    filename = f"invoices/invoice_{invoice.id}.pdf"
    with open(filename, 'rb') as file:
        attach_pdf = MIMEApplication(file.read(), _subtype="pdf")
        attach_pdf.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(attach_pdf)

    # Send Email
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, 'yourpassword')
        server.sendmail(sender_email, receiver_email, msg.as_string())
