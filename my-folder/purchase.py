"""
purchase.py
Handles stock purchasing operations.
"""

from datetime import datetime


class PurchaseManager:

    def __init__(self, product_manager, supplier_manager):

        self.product_manager = product_manager
        self.supplier_manager = supplier_manager

        self.purchase_history = []
        self.purchase_number = 5001

    # --------------------------------------------------

    def purchase_stock(self):

        print("\n========== PURCHASE STOCK ==========\n")

        supplier_id = int(input("Supplier ID: "))

        if supplier_id not in self.supplier_manager.suppliers:
            print("Supplier Not Found!")
            return

        supplier = self.supplier_manager.suppliers[supplier_id]

        product_id = int(input("Product ID: "))

        if product_id not in self.product_manager.products:
            print("Product Not Found!")
            return

        product = self.product_manager.products[product_id]

        quantity = int(input("Quantity Purchased: "))

        if quantity <= 0:
            print("Invalid Quantity!")
            return

        cost_price = float(
            input(
                f"Cost Price (Press Enter to use {product.cost_price}): "
            ) or product.cost_price
        )

        # Update product details
        product.quantity += quantity
        product.cost_price = cost_price

        total_cost = quantity * cost_price

        purchase = {
            "purchase_no": self.purchase_number,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "supplier": supplier.company_name,
            "supplier_id": supplier_id,
            "product": product.name,
            "product_id": product_id,
            "quantity": quantity,
            "cost_price": cost_price,
            "total_cost": total_cost
        }

        self.purchase_history.append(purchase)

        print("\nPurchase Recorded Successfully!")
        print("Updated Stock :", product.quantity)

        self.purchase_number += 1

    # --------------------------------------------------

    def view_purchase_history(self):

        if not self.purchase_history:
            print("\nNo Purchase Records Found!\n")
            return

        print("\n============== PURCHASE HISTORY ==============\n")

        for purchase in self.purchase_history:

            print(f"Purchase No : {purchase['purchase_no']}")
            print(f"Date        : {purchase['date']}")
            print(f"Supplier    : {purchase['supplier']}")
            print(f"Product     : {purchase['product']}")
            print(f"Quantity    : {purchase['quantity']}")
            print(f"Cost Price  : ₹{purchase['cost_price']}")
            print(f"Total Cost  : ₹{purchase['total_cost']:.2f}")

            print("-" * 50)

    # --------------------------------------------------

    def search_purchase(self):

        purchase_no = int(input("Purchase Number: "))

        for purchase in self.purchase_history:

            if purchase["purchase_no"] == purchase_no:

                print("\nPurchase Details\n")

                for key, value in purchase.items():
                    print(f"{key.replace('_',' ').title()} : {value}")

                return

        print("Purchase Record Not Found!")

    # --------------------------------------------------

    def supplier_report(self):

        supplier_id = int(input("Supplier ID: "))

        if supplier_id not in self.supplier_manager.suppliers:
            print("Supplier Not Found!")
            return

        supplier = self.supplier_manager.suppliers[supplier_id]

        print(f"\nPurchase Report for {supplier.company_name}\n")

        found = False
        total = 0

        for purchase in self.purchase_history:

            if purchase["supplier_id"] == supplier_id:

                found = True

                print(
                    f"{purchase['product']:<20}"
                    f"{purchase['quantity']:<10}"
                    f"₹{purchase['total_cost']:.2f}"
                )

                total += purchase["total_cost"]

        if not found:
            print("No Purchases Found.")
            return

        print("-" * 40)
        print("Total Purchase Amount : ₹", total)

    # --------------------------------------------------

    def total_purchase_cost(self):

        total = 0

        for purchase in self.purchase_history:
            total += purchase["total_cost"]

        return total

    # --------------------------------------------------

    def delete_purchase(self):

        purchase_no = int(input("Purchase Number: "))

        for i, purchase in enumerate(self.purchase_history):

            if purchase["purchase_no"] == purchase_no:

                confirm = input(
                    "Delete Purchase? (Y/N): "
                ).upper()

                if confirm == "Y":

                    del self.purchase_history[i]

                    print("Purchase Deleted Successfully!")

                else:

                    print("Deletion Cancelled!")

                return

        print("Purchase Record Not Found!")

    # --------------------------------------------------

    def purchase_summary(self):

        print("\n========== PURCHASE SUMMARY ==========\n")

        print("Total Purchases :", len(self.purchase_history))

        print(
            "Total Purchase Cost : ₹",
            round(self.total_purchase_cost(), 2)
        )
