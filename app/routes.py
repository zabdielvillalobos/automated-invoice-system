from flask import Blueprint, render_template, request, redirect, url_for
from .models import Invoice
from . import db
from .email_handler import send_invoice_email
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    invoices = Invoice.query.all()
    return render_template('dashboard.html', invoices=invoices)

@main.route('/new_invoice', methods=['GET', 'POST'])
def new_invoice():
    if request.method == 'POST':
        client_name = request.form['client_name']
        client_email = request.form['client_email']
        service_description = request.form['service_description']
        amount = request.form['amount']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')

        new_invoice = Invoice(client_name=client_name, client_email=client_email,
                              service_description=service_description, amount=amount,
                              due_date=due_date)

        db.session.add(new_invoice)
        db.session.commit()

        # Send Invoice Email
        send_invoice_email(new_invoice)

        return redirect(url_for('main.dashboard'))

    return render_template('new_invoice.html')

@main.route('/mark_paid/<int:invoice_id>')
def mark_paid(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    invoice.is_paid = True
    db.session.commit()
    return redirect(url_for('main.dashboard'))
