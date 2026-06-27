"""
reports.py
Generates business reports.
"""


class Reports:

    def __init__(self,
                 product_manager,
                 supplier_manager,
                 customer_manager,
                 inventory,
                 sales_manager,
                 purchase_manager):

        self.product_manager = product_manager
        self.supplier_manager = supplier_manager
        self.customer_manager = customer_manager
        self.inventory = inventory
        self.sales_manager = sales_manager
        self.purchase_manager = purchase_manager

    # --------------------------------------------------

    def inventory_report(self):

        print("\n" + "=" * 60)
        print("INVENTORY REPORT")
        print("=" * 60)

        self.product_manager.view_products()

        print()

        print(
            "Total Products :",
            self.product_manager.total_products()
        )

        print(
            "Inventory Value : ₹",
            round(
                self.product_manager.total_inventory_value(),
                2
            )
        )

    # --------------------------------------------------

    def sales_report(self):

        print("\n" + "=" * 60)
        print("SALES REPORT")
        print("=" * 60)

        print(
            "Invoices Generated :",
            len(self.sales_manager.sales_history)
        )

        print(
            "Revenue : ₹",
            round(
                self.sales_manager.total_revenue(),
                2
            )
        )

        print(
            "Profit : ₹",
            round(
                self.sales_manager.total_profit(),
                2
            )
        )

        print()

        self.sales_manager.best_selling_products()

    # --------------------------------------------------

    def purchase_report(self):

        print("\n" + "=" * 60)
        print("PURCHASE REPORT")
        print("=" * 60)

        print(
            "Total Purchases :",
            len(self.purchase_manager.purchase_history)
        )

        print(
            "Purchase Cost : ₹",
            round(
                self.purchase_manager.total_purchase_cost(),
                2
            )
        )

        print()

        self.purchase_manager.view_purchase_history()

    # --------------------------------------------------

    def supplier_report(self):

        print("\n" + "=" * 60)
        print("SUPPLIER REPORT")
        print("=" * 60)

        print(
            "Total Suppliers :",
            self.supplier_manager.total_suppliers()
        )

        print()

        self.supplier_manager.view_suppliers()

    # --------------------------------------------------

    def customer_report(self):

        print("\n" + "=" * 60)
        print("CUSTOMER REPORT")
        print("=" * 60)

        print(
            "Total Customers :",
            self.customer_manager.total_customers()
        )

        print()

        self.customer_manager.view_customers()

    # --------------------------------------------------

    def low_stock_report(self):

        print("\n" + "=" * 60)
        print("LOW STOCK REPORT")
        print("=" * 60)

        self.inventory.low_stock_alert()

    # --------------------------------------------------

    def out_of_stock_report(self):

        print("\n" + "=" * 60)
        print("OUT OF STOCK REPORT")
        print("=" * 60)

        self.inventory.out_of_stock()

    # --------------------------------------------------

    def category_report(self):

        print("\n" + "=" * 60)
        print("CATEGORY REPORT")
        print("=" * 60)

        self.inventory.category_report()

    # --------------------------------------------------

    def business_summary(self):

        print("\n" + "=" * 60)
        print("BUSINESS SUMMARY")
        print("=" * 60)

        revenue = self.sales_manager.total_revenue()

        purchase_cost = self.purchase_manager.total_purchase_cost()

        inventory_value = (
            self.product_manager.total_inventory_value()
        )

        profit = self.sales_manager.total_profit()

        print(f"Revenue           : ₹{revenue:.2f}")
        print(f"Purchase Cost     : ₹{purchase_cost:.2f}")
        print(f"Inventory Value   : ₹{inventory_value:.2f}")
        print(f"Estimated Profit  : ₹{profit:.2f}")

        print()

        print(
            "Products  :",
            self.product_manager.total_products()
        )

        print(
            "Customers :",
            self.customer_manager.total_customers()
        )

        print(
            "Suppliers :",
            self.supplier_manager.total_suppliers()
        )

        print(
            "Sales     :",
            len(self.sales_manager.sales_history)
        )

        print(
            "Purchases :",
            len(self.purchase_manager.purchase_history)
        )

    # --------------------------------------------------

    def all_reports(self):

        while True:

            print("\n" + "=" * 60)
            print("REPORTS MENU")
            print("=" * 60)

            print("1. Inventory Report")
            print("2. Sales Report")
            print("3. Purchase Report")
            print("4. Customer Report")
            print("5. Supplier Report")
            print("6. Low Stock Report")
            print("7. Out Of Stock Report")
            print("8. Category Report")
            print("9. Business Summary")
            print("0. Back")

            choice = input("\nEnter Choice : ")

            if choice == "1":
                self.inventory_report()

            elif choice == "2":
                self.sales_report()

            elif choice == "3":
                self.purchase_report()

            elif choice == "4":
                self.customer_report()

            elif choice == "5":
                self.supplier_report()

            elif choice == "6":
                self.low_stock_report()

            elif choice == "7":
                self.out_of_stock_report()

            elif choice == "8":
                self.category_report()

            elif choice == "9":
                self.business_summary()

            elif choice == "0":
                break

            else:
                print("Invalid Choice!")
