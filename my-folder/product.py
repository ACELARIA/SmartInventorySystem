"""
product.py
Handles all product-related operations.
"""


class Product:
    def __init__(self, product_id, name, category,
                 cost_price, selling_price,
                 quantity, supplier):

        self.product_id = product_id
        self.name = name
        self.category = category
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.quantity = quantity
        self.supplier = supplier

    def update_price(self, cost=None, selling=None):
        if cost is not None:
            self.cost_price = cost

        if selling is not None:
            self.selling_price = selling

    def update_stock(self, qty):
        self.quantity = qty

    def calculate_profit(self):
        return self.selling_price - self.cost_price

    def display(self):
        print(
            f"{self.product_id:<8}"
            f"{self.name:<20}"
            f"{self.category:<15}"
            f"{self.quantity:<10}"
            f"{self.cost_price:<12}"
            f"{self.selling_price:<12}"
            f"{self.supplier:<20}"
        )


class ProductManager:

    def __init__(self):
        self.products = {}

    # -----------------------------

    def add_product(self):

        product_id = int(input("Product ID: "))

        if product_id in self.products:
            print("Product ID already exists!")
            return

        name = input("Product Name: ")
        category = input("Category: ")

        cost = float(input("Cost Price: "))
        selling = float(input("Selling Price: "))

        qty = int(input("Quantity: "))

        supplier = input("Supplier: ")

        product = Product(
            product_id,
            name,
            category,
            cost,
            selling,
            qty,
            supplier
        )

        self.products[product_id] = product

        print("Product Added Successfully!")

    # -----------------------------

    def view_products(self):

        if not self.products:
            print("\nNo Products Found!\n")
            return

        print("-" * 100)

        print(
            f"{'ID':<8}"
            f"{'Name':<20}"
            f"{'Category':<15}"
            f"{'Qty':<10}"
            f"{'Cost':<12}"
            f"{'Sell':<12}"
            f"{'Supplier':<20}"
        )

        print("-" * 100)

        for product in self.products.values():
            product.display()

        print("-" * 100)

    # -----------------------------

    def search_product(self):

        choice = input(
            "Search by (1-ID / 2-Name): "
        )

        if choice == "1":

            pid = int(input("Enter Product ID: "))

            product = self.products.get(pid)

            if product:
                print()
                product.display()
            else:
                print("Product Not Found!")

        elif choice == "2":

            name = input("Enter Product Name: ").lower()

            found = False

            for product in self.products.values():

                if product.name.lower() == name:
                    product.display()
                    found = True

            if not found:
                print("Product Not Found!")

        else:
            print("Invalid Choice!")

    # -----------------------------

    def update_product(self):

        pid = int(input("Enter Product ID: "))

        if pid not in self.products:
            print("Product Not Found!")
            return

        product = self.products[pid]

        print()

        print("1. Update Cost Price")
        print("2. Update Selling Price")
        print("3. Update Quantity")
        print("4. Update Supplier")
        print("5. Update Category")

        choice = input("Choice: ")

        if choice == "1":
            product.cost_price = float(input("New Cost Price: "))

        elif choice == "2":
            product.selling_price = float(input("New Selling Price: "))

        elif choice == "3":
            product.quantity = int(input("New Quantity: "))

        elif choice == "4":
            product.supplier = input("New Supplier: ")

        elif choice == "5":
            product.category = input("New Category: ")

        else:
            print("Invalid Choice!")
            return

        print("Product Updated Successfully!")

    # -----------------------------

    def delete_product(self):

        pid = int(input("Enter Product ID: "))

        if pid not in self.products:
            print("Product Not Found!")
            return

        confirm = input(
            "Delete this product? (Y/N): "
        )

        if confirm.upper() == "Y":
            del self.products[pid]
            print("Product Deleted Successfully!")
        else:
            print("Deletion Cancelled!")

    # -----------------------------

    def low_stock(self):

        print("\nLOW STOCK PRODUCTS\n")

        found = False

        for product in self.products.values():

            if product.quantity < 5:
                product.display()
                found = True

        if not found:
            print("No Low Stock Products.")

    # -----------------------------

    def total_products(self):
        return len(self.products)

    # -----------------------------

    def total_inventory_value(self):

        total = 0

        for product in self.products.values():
            total += product.cost_price * product.quantity

        return total
