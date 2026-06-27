"""
billing.py
Handles invoice generation, display, saving, and searching.
"""

from datetime import datetime
import os


class Billing:

    def __init__(self):
        self.invoices = {}

    # --------------------------------------------------

    def generate_invoice(self,
                         invoice_no,
                         customer_name,
                         items,
                         subtotal,
                         discount,
                         gst):

        grand_total = subtotal - discount + gst

        invoice = {
            "invoice_no": invoice_no,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "customer": customer_name,
            "items": items,
            "subtotal": subtotal,
            "discount": discount,
            "gst": gst,
            "grand_total": grand_total
        }

        self.invoices[invoice_no] = invoice

        return invoice

    # --------------------------------------------------

    def print_invoice(self, invoice):

        print("\n")
        print("=" * 65)
        print("        SMART INVENTORY MANAGEMENT SYSTEM")
        print("=" * 65)

        print(f"Invoice No : {invoice['invoice_no']}")
        print(f"Date       : {invoice['date']}")
        print(f"Customer   : {invoice['customer']}")

        print("-" * 65)

        print(
            f"{'Product':<20}"
            f"{'Qty':<8}"
            f"{'Price':<12}"
            f"{'Total':<12}"
        )

        print("-" * 65)

        for item in invoice["items"]:

            print(
                f"{item['name']:<20}"
                f"{item['quantity']:<8}"
                f"{item['price']:<12.2f}"
                f"{item['total']:<12.2f}"
            )

        print("-" * 65)

        print(f"Subtotal    : ₹{invoice['subtotal']:.2f}")
        print(f"Discount    : ₹{invoice['discount']:.2f}")
        print(f"GST (18%)   : ₹{invoice['gst']:.2f}")
        print(f"Grand Total : ₹{invoice['grand_total']:.2f}")

        print("=" * 65)

    # --------------------------------------------------

    def save_invoice(self, invoice):

        filename = f"invoice_{invoice['invoice_no']}.txt"

        with open(filename, "w") as file:

            file.write("=" * 60 + "\n")
            file.write("SMART INVENTORY MANAGEMENT SYSTEM\n")
            file.write("=" * 60 + "\n\n")

            file.write(f"Invoice No : {invoice['invoice_no']}\n")
            file.write(f"Date       : {invoice['date']}\n")
            file.write(f"Customer   : {invoice['customer']}\n\n")

            file.write("-" * 60 + "\n")

            file.write(
                f"{'Product':<20}"
                f"{'Qty':<8}"
                f"{'Price':<10}"
                f"{'Total':<10}\n"
            )

            file.write("-" * 60 + "\n")

            for item in invoice["items"]:

                file.write(
                    f"{item['name']:<20}"
                    f"{item['quantity']:<8}"
                    f"{item['price']:<10.2f}"
                    f"{item['total']:<10.2f}\n"
                )

            file.write("-" * 60 + "\n")

            file.write(
                f"Subtotal    : ₹{invoice['subtotal']:.2f}\n"
            )

            file.write(
                f"Discount    : ₹{invoice['discount']:.2f}\n"
            )

            file.write(
                f"GST         : ₹{invoice['gst']:.2f}\n"
            )

            file.write(
                f"Grand Total : ₹{invoice['grand_total']:.2f}\n"
            )

        print(f"\nInvoice saved as {filename}")

    # --------------------------------------------------

    def search_invoice(self):

        invoice_no = int(input("Invoice Number: "))

        invoice = self.invoices.get(invoice_no)

        if invoice:
            self.print_invoice(invoice)
        else:
            print("Invoice Not Found!")

    # --------------------------------------------------

    def reprint_invoice(self):

        self.search_invoice()

    # --------------------------------------------------

    def delete_invoice(self):

        invoice_no = int(input("Invoice Number: "))

        if invoice_no not in self.invoices:
            print("Invoice Not Found!")
            return

        confirm = input(
            "Delete Invoice (Y/N): "
        ).upper()

        if confirm == "Y":

            del self.invoices[invoice_no]

            filename = f"invoice_{invoice_no}.txt"

            if os.path.exists(filename):
                os.remove(filename)

            print("Invoice Deleted Successfully!")

        else:

            print("Deletion Cancelled!")

    # --------------------------------------------------

    def list_invoices(self):

        if not self.invoices:
            print("No Invoices Available.")
            return

        print("\n=========== INVOICE LIST ===========\n")

        print(
            f"{'Invoice':<12}"
            f"{'Customer':<20}"
            f"{'Amount'}"
        )

        print("-" * 45)

        for invoice in self.invoices.values():

            print(
                f"{invoice['invoice_no']:<12}"
                f"{invoice['customer']:<20}"
                f"₹{invoice['grand_total']:.2f}"
            )

    # --------------------------------------------------

    def total_billing(self):

        total = 0

        for invoice in self.invoices.values():
            total += invoice["grand_total"]

        return total
