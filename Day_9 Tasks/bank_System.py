class BankAccount:
    # Initialize account number and optional starting balance
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    # Add funds if amount is positive
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}.")
        else:
            print("Invalid deposit amount.")

    # Deduct funds if sufficient balance exists
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}.")
        else:
            print("Insufficient balance or invalid amount.")

    # Show current balance
    def display_balance(self):
        print(f"Account: {self.account_number} | Balance: ₹{self.balance}")

acc = BankAccount("SB100234", int(input("Enter initial balance: ")))
acc.deposit(float(input("Enter deposit amount: ")))
acc.withdraw(float(input("Enter withdrawal amount: ")))
acc.display_balance()