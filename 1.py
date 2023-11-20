from module import BankAccount


account1 = BankAccount()
account1.display()

deposit_amount = float(input("Enter deposit amount: "))
account1.deposit(deposit_amount)

withdraw_amount = float(input("Enter withdrawal amount: "))
account1.withdraw(withdraw_amount)

account1.display()

    
