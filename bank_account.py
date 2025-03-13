# Bank Account System

class BankAccount:
    """A simple bank account class"""
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully!")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully!")

    def check_balance(self):
        """Display the account balance"""
        print(f"Account Balance: ${self.balance}")

# Create an account
my_account = BankAccount("John Doe", 1000)

# Perform transactions
my_account.deposit(500)
my_account.withdraw(200)
my_account.check_balance()