"""
customer.py
Handles customer management.
"""


class Customer:

    def __init__(self,
                 customer_id,
                 name,
                 phone,
                 email):

        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.purchase_history = []

    # ----------------------------

    def add_purchase(self, invoice):

        self.purchase_history.append(invoice)

    # ----------------------------

    def display(self):

        print(
            f"{self.customer_id:<10}"
            f"{self.name:<20}"
            f"{self.phone:<15}"
            f"{self.email:<30}"
        )


# ======================================================

class CustomerManager:

    def __init__(self):

        self.customers = {}

    # --------------------------------------------------

    def add_customer(self):

        customer_id = int(input("Customer ID: "))

        if customer_id in self.customers:
            print("Customer already exists!")
            return

        name = input("Customer Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        customer = Customer(
            customer_id,
            name,
            phone,
            email
        )

        self.customers[customer_id] = customer

        print("Customer Added Successfully!")

    # --------------------------------------------------

    def view_customers(self):

        if not self.customers:
            print("\nNo Customers Found.\n")
            return

        print("-" * 80)

        print(
            f"{'ID':<10}"
            f"{'Name':<20}"
            f"{'Phone':<15}"
            f"{'Email':<30}"
        )

        print("-" * 80)

        for customer in self.customers.values():
            customer.display()

        print("-" * 80)

    # --------------------------------------------------

    def search_customer(self):

        choice = input(
            "\nSearch By\n"
            "1. Customer ID\n"
            "2. Customer Name\n"
            "Choice: "
        )

        if choice == "1":

            cid = int(input("Customer ID: "))

            customer = self.customers.get(cid)

            if customer:
                customer.display()
            else:
                print("Customer Not Found!")

        elif choice == "2":

            name = input("Customer Name: ").lower()

            found = False

            for customer in self.customers.values():

                if customer.name.lower() == name:
                    customer.display()
                    found = True

            if not found:
                print("Customer Not Found!")

        else:
            print("Invalid Choice!")

    # --------------------------------------------------

    def update_customer(self):

        cid = int(input("Customer ID: "))

        if cid not in self.customers:
            print("Customer Not Found!")
            return

        customer = self.customers[cid]

        print("\n1. Name")
        print("2. Phone")
        print("3. Email")

        choice = input("Choice: ")

        if choice == "1":
            customer.name = input("New Name: ")

        elif choice == "2":
            customer.phone = input("New Phone: ")

        elif choice == "3":
            customer.email = input("New Email: ")

        else:
            print("Invalid Choice!")
            return

        print("Customer Updated Successfully!")

    # --------------------------------------------------

    def delete_customer(self):

        cid = int(input("Customer ID: "))

        if cid not in self.customers:
            print("Customer Not Found!")
            return

        confirm = input("Delete Customer (Y/N): ")

        if confirm.upper() == "Y":

            del self.customers[cid]

            print("Customer Deleted Successfully!")

        else:

            print("Deletion Cancelled!")

    # --------------------------------------------------

    def add_purchase_history(self, customer_id, invoice):

        if customer_id in self.customers:
            self.customers[customer_id].add_purchase(invoice)

    # --------------------------------------------------

    def view_purchase_history(self):

        cid = int(input("Customer ID: "))

        if cid not in self.customers:
            print("Customer Not Found!")
            return

        customer = self.customers[cid]

        print("\nPurchase History")
        print("-" * 40)

        if not customer.purchase_history:
            print("No Purchases Yet.")
            return

        for invoice in customer.purchase_history:
            print(invoice)

    # --------------------------------------------------

    def total_customers(self):

        return len(self.customers)
