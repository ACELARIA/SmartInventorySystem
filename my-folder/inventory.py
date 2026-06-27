"""
inventory.py
Handles inventory operations.
"""

from product import ProductManager


class Inventory:

    def __init__(self, product_manager: ProductManager):
        self.product_manager = product_manager

    # -----------------------------------------

    def view_current_stock(self):

        if not self.product_manager.products:
            print("\nNo Products Available.\n")
            return

        print("\n========== CURRENT STOCK ==========")

        print(f"{'ID':<8}{'Product':<20}{'Stock':<10}")

        print("-" * 40)

        for product in self.product_manager.products.values():

            print(
                f"{product.product_id:<8}"
                f"{product.name:<20}"
                f"{product.quantity:<10}"
            )

    # -----------------------------------------

    def restock_product(self):

        pid = int(input("Enter Product ID: "))

        if pid not in self.product_manager.products:
            print("Product Not Found!")
            return

        qty = int(input("Quantity to Add: "))

        self.product_manager.products[pid].quantity += qty

        print("Stock Updated Successfully!")

        print(
            "Current Stock:",
            self.product_manager.products[pid].quantity
        )

    # -----------------------------------------

    def reduce_stock(self, product_id, qty):

        if product_id not in self.product_manager.products:
            return False

        product = self.product_manager.products[product_id]

        if qty > product.quantity:
            return False

        product.quantity -= qty

        return True

    # -----------------------------------------

    def low_stock_alert(self):

        found = False

        print("\n========== LOW STOCK ALERT ==========\n")

        for product in self.product_manager.products.values():

            if product.quantity < 5:

                found = True

                print(
                    f"{product.name}"
                    f" (ID:{product.product_id})"
                )

                print(f"Remaining Stock : {product.quantity}")

                print("-" * 30)

        if not found:
            print("No Low Stock Products.")

    # -----------------------------------------

    def out_of_stock(self):

        found = False

        print("\n====== OUT OF STOCK ======\n")

        for product in self.product_manager.products.values():

            if product.quantity == 0:

                found = True

                print(product.name)

        if not found:
            print("No Out-of-Stock Products.")

    # -----------------------------------------

    def inventory_value(self):

        total = 0

        for product in self.product_manager.products.values():

            total += (
                product.cost_price *
                product.quantity
            )

        print("\nTotal Inventory Value : ₹", total)

        return total

    # -----------------------------------------

    def category_report(self):

        report = {}

        for product in self.product_manager.products.values():

            if product.category not in report:
                report[product.category] = 0

            report[product.category] += 1

        print("\n======= CATEGORY REPORT =======")

        for category, count in report.items():

            print(f"{category:<20}{count} Products")

    # -----------------------------------------

    def stock_summary(self):

        total_products = len(
            self.product_manager.products
        )

        total_stock = 0

        for product in self.product_manager.products.values():

            total_stock += product.quantity

        print("\n========== STOCK SUMMARY ==========")

        print("Total Products :", total_products)

        print("Total Stock :", total_stock)

        self.inventory_value()
