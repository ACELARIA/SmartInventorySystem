"""
authentication.py
-----------------
Handles user authentication for the Smart Inventory Management System.
"""


class Authentication:
    def __init__(self):
        # Default admin credentials
        self.username = "admin"
        self.password = "admin123"
        self.max_attempts = 3

    def login(self):
        """Authenticate user with maximum 3 attempts."""
        attempts = 0

        print("=" * 50)
        print("      SMART INVENTORY MANAGEMENT SYSTEM")
        print("=" * 50)

        while attempts < self.max_attempts:
            username = input("Username: ")
            password = input("Password: ")

            if username == self.username and password == self.password:
                print("\nLogin Successful!\n")
                return True

            attempts += 1
            remaining = self.max_attempts - attempts

            if remaining > 0:
                print(f"\nInvalid Credentials!")
                print(f"Attempts Remaining: {remaining}\n")

        print("\nToo many failed attempts!")
        print("System Closed.")
        return False
