class Payment:
    # Base method overridden by subclasses
    def process_payment(self, amount):
        print(f"Processing generic payment of ₹{amount}")

class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UPI(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI.")

class NetBanking(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} through NetBanking.")

payments = [CreditCard(), UPI(), NetBanking()]

# Resolved dynamically at runtime per object
for method in payments:
    method.process_payment(1200)