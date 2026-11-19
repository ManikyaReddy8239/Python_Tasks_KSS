'''4. Bank Account System (Class, Object, Constructor) 
A bank wants to manage customer accounts. Create a BankAccount class with a 
constructor to initialize account number and balance.
Implement methods to deposit, withdraw, and display balance. '''

class BankAccount():
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount has been deposited:",amount)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
            print("Withdrawl amount:",amount)
        else:
            print("Insufficient balance:")
    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Available Balance:", self.balance)
obj=BankAccount(1234,5000)
obj.deposit(2000)
obj.withdraw(1000)
obj.display_balance()
