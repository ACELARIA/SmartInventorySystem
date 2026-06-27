"""
main.py
Smart Inventory Management System
"""

from authentication import Authentication
from product import ProductManager
from supplier import SupplierManager
from customer import CustomerManager
from inventory import Inventory
from sales import SalesManager
from purchase import PurchaseManager
from billing import Billing
from reports import Reports


# ===========================================================
# Create Objects
# ===========================================================

auth = Authentication()

product_manager = ProductManager()

supplier_manager = SupplierManager()

customer_manager = CustomerManager()

inventory = Inventory(product_manager)

sales_manager = SalesManager(
    product_manager,
    customer_manager,
    inventory
)

purchase_manager = PurchaseManager(
    product_manager,
    supplier_manager
)

billing = Billing()

reports = Reports(
    product_manager,
    supplier_manager,
    customer_manager,
    inventory,
    sales_manager,
    purchase_manager
)


# ===========================================================
# Product Menu
# ===========================================================

def product_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("PRODUCT MANAGEMENT")
        print("=" * 50)

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Low Stock Products")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            product_manager.add_product()

        elif choice == "2":
            product_manager.view_products()

        elif choice == "3":
            product_manager.search_product()

        elif choice == "4":
            product_manager.update_product()

        elif choice == "5":
            product_manager.delete_product()

        elif choice == "6":
            product_manager.low_stock()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")


# ===========================================================
# Supplier Menu
# ===========================================================

def supplier_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("SUPPLIER MANAGEMENT")
        print("=" * 50)

        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Search Supplier")
        print("4. Update Supplier")
        print("5. Delete Supplier")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            supplier_manager.add_supplier()

        elif choice == "2":
            supplier_manager.view_suppliers()

        elif choice == "3":
            supplier_manager.search_supplier()

        elif choice == "4":
            supplier_manager.update_supplier()

        elif choice == "5":
            supplier_manager.delete_supplier()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")


# ===========================================================
# Customer Menu
# ===========================================================

def customer_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("CUSTOMER MANAGEMENT")
        print("=" * 50)

        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Purchase History")
        print("6. Delete Customer")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            customer_manager.add_customer()

        elif choice == "2":
            customer_manager.view_customers()

        elif choice == "3":
            customer_manager.search_customer()

        elif choice == "4":
            customer_manager.update_customer()

        elif choice == "5":
            customer_manager.view_purchase_history()

        elif choice == "6":
            customer_manager.delete_customer()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")
            # ===========================================================
# Inventory Menu
# ===========================================================

def inventory_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("INVENTORY MANAGEMENT")
        print("=" * 50)

        print("1. View Current Stock")
        print("2. Restock Product")
        print("3. Low Stock Alert")
        print("4. Out of Stock")
        print("5. Inventory Value")
        print("6. Category Report")
        print("7. Stock Summary")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            inventory.view_current_stock()

        elif choice == "2":
            inventory.restock_product()

        elif choice == "3":
            inventory.low_stock_alert()

        elif choice == "4":
            inventory.out_of_stock()

        elif choice == "5":
            inventory.inventory_value()

        elif choice == "6":
            inventory.category_report()

        elif choice == "7":
            inventory.stock_summary()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")


# ===========================================================
# Sales Menu
# ===========================================================

def sales_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("SALES MANAGEMENT")
        print("=" * 50)

        print("1. Sell Product")
        print("2. View Sales History")
        print("3. Search Invoice")
        print("4. Daily Sales Report")
        print("5. Best Selling Products")
        print("6. Sales Summary")
        print("7. Delete Sale")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            sales_manager.sell_product()

        elif choice == "2":
            sales_manager.view_sales_history()

        elif choice == "3":
            sales_manager.search_invoice()

        elif choice == "4":
            sales_manager.daily_sales_report()

        elif choice == "5":
            sales_manager.best_selling_products()

        elif choice == "6":
            sales_manager.sales_summary()

        elif choice == "7":
            sales_manager.delete_sale()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")


# ===========================================================
# Purchase Menu
# ===========================================================

def purchase_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("PURCHASE MANAGEMENT")
        print("=" * 50)

        print("1. Purchase Stock")
        print("2. View Purchase History")
        print("3. Search Purchase")
        print("4. Supplier Purchase Report")
        print("5. Purchase Summary")
        print("6. Delete Purchase")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            purchase_manager.purchase_stock()

        elif choice == "2":
            purchase_manager.view_purchase_history()

        elif choice == "3":
            purchase_manager.search_purchase()

        elif choice == "4":
            purchase_manager.supplier_report()

        elif choice == "5":
            purchase_manager.purchase_summary()

        elif choice == "6":
            purchase_manager.delete_purchase()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")
            # ===========================================================
# Billing Menu
# ===========================================================

def billing_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("BILLING")
        print("=" * 50)

        print("1. List Saved Invoices")
        print("2. Search Invoice")
        print("3. Reprint Invoice")
        print("4. Delete Invoice")
        print("5. Total Billing")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            billing.list_invoices()

        elif choice == "2":
            billing.search_invoice()

        elif choice == "3":
            billing.reprint_invoice()

        elif choice == "4":
            billing.delete_invoice()

        elif choice == "5":
            print(
                "Total Billing : ₹",
                round(billing.total_billing(), 2)
            )

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")


# ===========================================================
# Reports Menu
# ===========================================================

def reports_menu():

    reports.all_reports()


# ===========================================================
# Main Menu
# ===========================================================

def main_menu():

    while True:

        print("\n")
        print("=" * 60)
        print(" SMART INVENTORY MANAGEMENT SYSTEM ")
        print("=" * 60)

        print("1. Product Management")
        print("2. Inventory Management")
        print("3. Supplier Management")
        print("4. Customer Management")
        print("5. Sales Management")
        print("6. Purchase Management")
        print("7. Billing")
        print("8. Reports")
        print("9. Logout")
        print("0. Exit")

        print("=" * 60)

        choice = input("Enter Choice : ")

        if choice == "1":
            product_menu()

        elif choice == "2":
            inventory_menu()

        elif choice == "3":
            supplier_menu()

        elif choice == "4":
            customer_menu()

        elif choice == "5":
            sales_menu()

        elif choice == "6":
            purchase_menu()

        elif choice == "7":
            billing_menu()

        elif choice == "8":
            reports_menu()

        elif choice == "9":

            print("\nLogging Out...\n")

            if auth.login():
                continue
            else:
                break

        elif choice == "0":

            print("\nThank You For Using Smart Inventory System.")
            print("Goodbye!")

            break

        else:
            print("Invalid Choice!")


# ===========================================================
# Program Entry
# ===========================================================

def main():

    if auth.login():
        main_menu()
    else:
        print("Access Denied.")


# ===========================================================

if __name__ == "__main__":
    main()
