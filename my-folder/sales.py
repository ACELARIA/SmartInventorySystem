"""
sales.py
Handles all sales operations.
"""

from datetime import datetime


class SalesManager:

    def __init__(self, product_manager,
                 customer_manager,
                 inventory):

        self.product_manager = product_manager
        self.customer_manager = customer_manager
        self.inventory = inventory

        self.sales_history = []
        self.invoice_number = 1001

    # ---------------------------------------------------

    def calculate_discount(self, subtotal):

        if subtotal >= 10000:
            return subtotal * 0.15

        elif subtotal >= 5000:
            return subtotal * 0.10

        elif subtotal >= 2000:
            return subtotal * 0.05

        return 0

    # ---------------------------------------------------

    def calculate_gst(self, amount):

        return amount * 0.18

    # ---------------------------------------------------

    def sell_product(self):

        print("\n========== SALES ==========\n")

        customer_id = int(input("Customer ID: "))

        if customer_id not in self.customer_manager.customers:
            print("Customer Not Found!")
            return

        customer = self.customer_manager.customers[customer_id]

        invoice_items = []

        subtotal = 0

        while True:

            product_id = int(input("\nProduct ID: "))

            if product_id not in self.product_manager.products:
                print("Invalid Product ID")
                continue

            product = self.product_manager.products[product_id]

            print("Product :", product.name)
            print("Available Stock :", product.quantity)

            quantity = int(input("Quantity: "))

            if quantity <= 0:
                print("Invalid Quantity")
                continue

            if quantity > product.quantity:
                print("Insufficient Stock!")
                continue

            total = quantity * product.selling_price

            invoice_items.append({
                "id": product.product_id,
                "name": product.name,
                "price": product.selling_price,
                "quantity": quantity,
                "total": total
            })

            subtotal += total

            # Reduce stock
            self.inventory.reduce_stock(product_id, quantity)

            choice = input(
                "\nAdd Another Product? (Y/N): "
            ).upper()

            if choice != "Y":
                break

        if len(invoice_items) == 0:
            print("No Sale Completed.")
            return

        discount = self.calculate_discount(subtotal)

        taxable = subtotal - discount

        gst = self.calculate_gst(taxable)

        grand_total = taxable + gst

        invoice = {
            "invoice_no": self.invoice_number,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "customer_id": customer.customer_id,
            "customer_name": customer.name,
            "items": invoice_items,
            "subtotal": subtotal,
            "discount": discount,
            "gst": gst,
            "grand_total": grand_total
        }

        self.sales_history.append(invoice)

        customer.add_purchase(invoice)

        self.print_invoice(invoice)

        self.invoice_number += 1

    # ---------------------------------------------------

    def print_invoice(self, invoice):

        print("\n")
        print("=" * 60)
        print("SMART INVENTORY MANAGEMENT SYSTEM")
        print("=" * 60)

        print("Invoice No :", invoice["invoice_no"])
        print("Date       :", invoice["date"])
        print("Customer   :", invoice["customer_name"])

        print("-" * 60)

        print(
            f"{'Product':<20}"
            f"{'Qty':<8}"
            f"{'Price':<10}"
            f"{'Total':<10}"
        )

        print("-" * 60)

        for item in invoice["items"]:

            print(
                f"{item['name']:<20}"
                f"{item['quantity']:<8}"
                f"{item['price']:<10}"
                f"{item['total']:<10}"
            )

        print("-" * 60)

        print(f"Subtotal   : ₹{invoice['subtotal']:.2f}")
        print(f"Discount   : ₹{invoice['discount']:.2f}")
        print(f"GST (18%)  : ₹{invoice['gst']:.2f}")

        print("-" * 60)

        print(
            f"Grand Total: ₹{invoice['grand_total']:.2f}"
        )

        print("=" * 60)
            # ---------------------------------------------------

    def view_sales_history(self):

        if not self.sales_history:
            print("\nNo Sales Found!\n")
            return

        print("\n================ SALES HISTORY ================\n")

        for sale in self.sales_history:

            print(f"Invoice No : {sale['invoice_no']}")
            print(f"Date       : {sale['date']}")
            print(f"Customer   : {sale['customer_name']}")
            print(f"Amount     : ₹{sale['grand_total']:.2f}")

            print("-" * 50)

    # ---------------------------------------------------

    def search_invoice(self):

        invoice_no = int(input("Enter Invoice Number: "))

        for sale in self.sales_history:

            if sale["invoice_no"] == invoice_no:

                self.print_invoice(sale)
                return

        print("Invoice Not Found!")

    # ---------------------------------------------------

    def total_revenue(self):

        revenue = 0

        for sale in self.sales_history:
            revenue += sale["grand_total"]

        return revenue

    # ---------------------------------------------------

    def total_profit(self):

        profit = 0

        for sale in self.sales_history:

            for item in sale["items"]:

                product = self.product_manager.products[item["id"]]

                profit += (
                    product.selling_price
                    - product.cost_price
                ) * item["quantity"]

        return profit

    # ---------------------------------------------------

    def daily_sales_report(self):

        print("\n========== DAILY SALES REPORT ==========\n")

        print("Total Sales :", len(self.sales_history))

        print(
            "Revenue : ₹",
            round(self.total_revenue(), 2)
        )

        print(
            "Profit : ₹",
            round(self.total_profit(), 2)
        )

    # ---------------------------------------------------

    def best_selling_products(self):

        if not self.sales_history:
            print("No Sales Yet.")
            return

        product_count = {}

        for sale in self.sales_history:

            for item in sale["items"]:

                pid = item["id"]

                if pid not in product_count:
                    product_count[pid] = 0

                product_count[pid] += item["quantity"]

        print("\n======= BEST SELLING PRODUCTS =======\n")

        ranking = sorted(
            product_count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        print(
            f"{'Product':<20}"
            f"{'Units Sold'}"
        )

        print("-" * 35)

        for pid, qty in ranking:

            product = self.product_manager.products[pid]

            print(
                f"{product.name:<20}"
                f"{qty}"
            )

    # ---------------------------------------------------

    def delete_sale(self):

        invoice_no = int(input("Invoice Number: "))

        for i, sale in enumerate(self.sales_history):

            if sale["invoice_no"] == invoice_no:

                confirm = input(
                    "Delete Sale (Y/N): "
                ).upper()

                if confirm == "Y":

                    del self.sales_history[i]

                    print("Sale Deleted Successfully!")

                else:

                    print("Deletion Cancelled!")

                return

        print("Invoice Not Found!")

    # ---------------------------------------------------

    def sales_summary(self):

        print("\n========== SALES SUMMARY ==========\n")

        print("Invoices Generated :", len(self.sales_history))

        print(
            "Total Revenue : ₹",
            round(self.total_revenue(), 2)
        )

        print(
            "Total Profit : ₹",
            round(self.total_profit(), 2)
        )

        self.best_selling_products()
