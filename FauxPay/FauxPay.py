import smtplib
import random
import sys
from email.mime.text import MIMEText
from fpdf import FPDF
from rich.console import Console
from rich.table import Table

console = Console()

# Define some fake payment templates for message generation
payment_templates = [
    "Payment of ${amount} has been successfully sent to {receiver} on {date}. Ref#: TXN{txn_id}",
    "Transaction complete. ${amount} was transferred to {receiver} on {date}. Ref#: TXN{txn_id}"
]

# Function to generate a random transaction ID
def generate_txn_id():
    return random.randint(100000, 999999)

# Function to generate a fake payment message
def generate_payment_message(receiver, amount, date):
    template = random.choice(payment_templates)
    txn_id = generate_txn_id()
    return template.format(receiver=receiver, amount=amount, date=date, txn_id=txn_id)

# Function to send an email using SMTP
def send_email(receiver_email, subject, message, smtp_server, smtp_port, smtp_user, smtp_password):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, receiver_email, msg.as_string())
        console.print(f":white_check_mark: Email successfully sent to [bold]{receiver_email}[/bold]", style="green")
    except Exception as e:
        console.print(f":x: Failed to send email: {e}", style="red")

# Function to generate an invoice PDF
def generate_invoice_pdf(client_name, client_address, client_email, invoice_date, invoice_number, items):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "INVOICE", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Date: {invoice_date}", ln=True)
    pdf.cell(200, 10, f"Invoice #: {invoice_number}", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, "Bill To:", ln=True)
    pdf.cell(200, 10, f"{client_name}", ln=True)
    pdf.cell(200, 10, f"{client_address}", ln=True)
    pdf.cell(200, 10, f"{client_email}", ln=True)
    pdf.ln(10)
    
    # Table Header
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(80, 10, "Description", border=1)
    pdf.cell(40, 10, "Quantity", border=1)
    pdf.cell(40, 10, "Unit Price", border=1)
    pdf.cell(30, 10, "Total", border=1)
    pdf.ln(10)
    
    # Table Content
    pdf.set_font("Arial", size=12)
    total_amount = 0.0
    for item in items:
        description, quantity, unit_price = item
        try:
            total = float(quantity) * float(unit_price)
        except ValueError:
            console.print(f":warning: Invalid quantity or unit price for item '{description}'. Skipping this item.", style="yellow")
            continue
        total_amount += total
        pdf.cell(80, 10, description, border=1)
        pdf.cell(40, 10, str(quantity), border=1)
        pdf.cell(40, 10, f"${unit_price}", border=1)
        pdf.cell(30, 10, f"${total:.2f}", border=1)
        pdf.ln(10)
    
    # Total Amount
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(160, 10, "Total", border=1)
    pdf.cell(30, 10, f"${total_amount:.2f}", border=1)
    pdf.ln(20)
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Please make payment by the due date. Thank you for your business!", ln=True)
    
    pdf.output(f"Invoice_{client_name.replace(' ', '_')}.pdf")
    console.print(f":white_check_mark: PDF invoice successfully generated: [bold]Invoice_{client_name.replace(' ', '_')}.pdf[/bold]", style="green")

# Main function to handle user input and run the script
def main():
    while True:
        console.print("\n[bold cyan]FauxPay - Digital Payment & Invoice Generation CLI[/bold cyan]")
        console.print("1. Generate Fake Payment Message")
        console.print("2. Send Fake Payment Email")
        console.print("3. Generate Payment Confirmation PDF")
        console.print("4. Generate Invoice PDF")
        console.print("5. View Previous Invoices")
        console.print("6. View Payment Summary")
        console.print("7. Generate Custom Report PDF")
        console.print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            receiver = input("Enter receiver name: ")
            amount = input("Enter amount of payment: ")
            date = input("Enter transaction date: ")
            message = generate_payment_message(receiver, amount, date)
            console.print(f"\nGenerated Message:\n[bold]{message}[/bold]", style="cyan")

        elif choice == '2':
            receiver = input("Enter receiver name: ")
            amount = input("Enter amount of payment: ")
            date = input("Enter transaction date: ")
            email = input("Enter receiver email address: ")
            smtp_server = input("Enter SMTP server address: ")
            smtp_port = int(input("Enter SMTP server port: "))
            smtp_user = input("Enter SMTP server username: ")
            smtp_password = input("Enter SMTP server password: ")
            
            message = generate_payment_message(receiver, amount, date)
            send_email(email, "Payment Confirmation", message, smtp_server, smtp_port, smtp_user, smtp_password)

        elif choice == '3':
            receiver = input("Enter receiver name: ")
            amount = input("Enter amount of payment: ")
            date = input("Enter transaction date: ")
            generate_pdf(receiver, amount, date)

        elif choice == '4':
            client_name = input("Enter client name: ")
            client_address = input("Enter client address: ")
            client_email = input("Enter client email: ")
            invoice_date = input("Enter invoice date: ")
            invoice_number = input("Enter invoice number: ")
            items = []
            while True:
                description = input("Enter item description (or 'done' to finish): ")
                if description.lower() == 'done':
                    break
                quantity = input("Enter quantity: ")
                unit_price = input("Enter unit price: ")
                items.append((description, quantity, unit_price))
            generate_invoice_pdf(client_name, client_address, client_email, invoice_date, invoice_number, items)

        elif choice == '5':
            console.print("Feature to view previous invoices is under construction.", style="yellow")

        elif choice == '6':
            console.print("Feature to view payment summary is under construction.", style="yellow")

        elif choice == '7':
            console.print("Feature to generate custom report PDF is under construction.", style="yellow")

        elif choice == '8':
            console.print("Exiting the program.", style="red")
            sys.exit(0)
        else:
            console.print("Invalid choice. Please enter a number between 1 and 8.", style="red")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        console.print(f":x: An unexpected error occurred: {e}", style="red")
        sys.exit(1)
