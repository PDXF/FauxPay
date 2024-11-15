# FauxPay - Digital Payment & Invoice Generation CLI

**FauxPay** is a command-line tool designed to generate fake payment messages, send payment confirmation emails, and create professional-looking invoices in PDF format. It can be useful for testing, demonstration purposes, or scenarios where placeholder financial documents are needed.

## Features

- **Generate Fake Payment Message**: Create a custom payment message with transaction details.
- **Send Fake Payment Email**: Send a payment confirmation email to a recipient.
- **Generate Payment Confirmation PDF**: Produce a simple payment confirmation PDF document.
- **Generate Invoice PDF**: Create a detailed invoice with client information and itemized billing.
- **View Previous Invoices** (Coming Soon): Browse generated invoices.
- **View Payment Summary** (Coming Soon): Review the overall payment activity.
- **Generate Custom Report PDF** (Coming Soon): Create custom PDF reports for financial records.

## Prerequisites

- **Python 3.x**: Make sure Python is installed on your machine.
- **Required Python Packages**:
  - `rich`: For enhanced CLI visual presentation.
  - `fpdf`: To generate PDFs for invoices and confirmations.
  - `smtplib`: Standard library for sending emails.

Install the required packages by running:

```sh
pip install rich fpdf
```

## How to Use

1. **Clone the Repository**

   ```sh
   git clone https://github.com/PDXF/FauxPay.git
   cd FauxPay
   ```

2. **Run FauxPay**

   You can use the provided batch script (`run_fauxpay.bat`) to start FauxPay easily:

   ```sh
   run_fauxpay.bat
   ```

   Alternatively, run the Python script directly:

   ```sh
   python FauxPay.py
   ```

3. **Interact with the Menu**

   FauxPay presents an interactive menu with the following options:
   - **1**: Generate a fake payment message.
   - **2**: Send a fake payment email.
   - **3**: Generate a payment confirmation PDF.
   - **4**: Generate an invoice PDF.
   - **5**: View previous invoices (Coming Soon).
   - **6**: View payment summary (Coming Soon).
   - **7**: Generate a custom report PDF (Coming Soon).
   - **8**: Exit the application.

## Example Usage

### Generate an Invoice PDF

1. Select option **4** from the main menu.
2. Enter the client details:
   - Client name
   - Client address
   - Client email
   - Invoice date
   - Invoice number
3. Provide item descriptions, quantities, and unit prices. Type 'done' when finished.
4. The generated invoice will be saved as a PDF file in the current directory.

## Batch Script for Easy Execution

The batch script `run_fauxpay.bat` is included for easy execution on Windows systems. Simply double-click the batch file to start FauxPay.

## Notes

- **Email Functionality**: To send emails, you need SMTP credentials (e.g., SMTP server, port, username, and password). Ensure that these details are correctly entered when using the email feature.
- **Disclaimer**: FauxPay is for testing and demonstration purposes only. Do not use this tool for any unlawful activities.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


