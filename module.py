class BankAccount:
    def __init__(self):
        self.accountNumber = input("Enter Account Number: ")
        self.customerName = input("Enter Customer Name: ")
        self.balance = float(input("Enter Initial Balance: "))  # Assuming balance is a float

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal not allowed.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Customer Name: {self.customerName}")
        print(f"Balance: ${self.balance}")

