"""
supplier.py
Handles supplier management.
"""


class Supplier:

    def __init__(self,
                 supplier_id,
                 company_name,
                 phone,
                 email,
                 address):

        self.supplier_id = supplier_id
        self.company_name = company_name
        self.phone = phone
        self.email = email
        self.address = address

    def display(self):

        print(
            f"{self.supplier_id:<10}"
            f"{self.company_name:<25}"
            f"{self.phone:<15}"
            f"{self.email:<30}"
            f"{self.address:<30}"
        )


class SupplierManager:

    def __init__(self):
        self.suppliers = {}

    # ---------------------------------

    def add_supplier(self):

        supplier_id = int(input("Supplier ID: "))

        if supplier_id in self.suppliers:
            print("Supplier ID already exists!")
            return

        company = input("Company Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")

        supplier = Supplier(
            supplier_id,
            company,
            phone,
            email,
            address
        )

        self.suppliers[supplier_id] = supplier

        print("\nSupplier Added Successfully!")

    # ---------------------------------

    def view_suppliers(self):

        if not self.suppliers:
            print("\nNo Suppliers Available.\n")
            return

        print("-" * 115)

        print(
            f"{'ID':<10}"
            f"{'Company':<25}"
            f"{'Phone':<15}"
            f"{'Email':<30}"
            f"{'Address':<30}"
        )

        print("-" * 115)

        for supplier in self.suppliers.values():
            supplier.display()

        print("-" * 115)

    # ---------------------------------

    def search_supplier(self):

        choice = input(
            "\nSearch By\n"
            "1. Supplier ID\n"
            "2. Company Name\n"
            "Choice: "
        )

        if choice == "1":

            supplier_id = int(input("Enter Supplier ID: "))

            supplier = self.suppliers.get(supplier_id)

            if supplier:
                print()
                supplier.display()
            else:
                print("Supplier Not Found!")

        elif choice == "2":

            company = input("Company Name: ").lower()

            found = False

            for supplier in self.suppliers.values():

                if supplier.company_name.lower() == company:
                    supplier.display()
                    found = True

            if not found:
                print("Supplier Not Found!")

        else:
            print("Invalid Choice!")

    # ---------------------------------

    def update_supplier(self):

        supplier_id = int(input("Supplier ID: "))

        if supplier_id not in self.suppliers:
            print("Supplier Not Found!")
            return

        supplier = self.suppliers[supplier_id]

        print("\n1. Company Name")
        print("2. Phone")
        print("3. Email")
        print("4. Address")

        choice = input("Choice: ")

        if choice == "1":
            supplier.company_name = input("New Company Name: ")

        elif choice == "2":
            supplier.phone = input("New Phone: ")

        elif choice == "3":
            supplier.email = input("New Email: ")

        elif choice == "4":
            supplier.address = input("New Address: ")

        else:
            print("Invalid Choice!")
            return

        print("Supplier Updated Successfully!")

    # ---------------------------------

    def delete_supplier(self):

        supplier_id = int(input("Supplier ID: "))

        if supplier_id not in self.suppliers:
            print("Supplier Not Found!")
            return

        confirm = input("Delete Supplier? (Y/N): ")

        if confirm.upper() == "Y":
            del self.suppliers[supplier_id]
            print("Supplier Deleted Successfully!")

        else:
            print("Deletion Cancelled!")

    # ---------------------------------

    def total_suppliers(self):
        return len(self.suppliers)
