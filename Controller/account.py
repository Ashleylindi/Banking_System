# models/account.py

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def create_account(self):
        # Logic to create a new account
        print("Account created successfully.")

    def delete_account(self):
        # Logic to delete the account
        print("Account deleted successfully.")

    def show_account_status(self):
        # Logic to display account status
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

    def give_proof_of_account(self):
        # Logic to provide proof of account
        print("Proof of account provided.")


