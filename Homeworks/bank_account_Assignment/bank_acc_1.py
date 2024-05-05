from abc import ABC,abstractmethod
class BankAccount:
    # Constructor to initialize the attributes
    def __init__(self, interest_rate=0.0, balance=0.0):
        self.interest_rate = interest_rate
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        return self

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self

    # Method to display the account information
    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest Rate: {self.interest_rate}%")

    # Method to yield interest on the account balance
    def yield_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)
        return self

    # Class method to print info of all instances of BankAccount
    @classmethod
    def print_all_accounts_info(cls, accounts):
        for account in accounts:
            account.display_account_info()

# Create two accounts
account1 = BankAccount(interest_rate=5)
account2 = BankAccount(interest_rate=3)

# Perform operations on the first account
account1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()

# Perform operations on the second account
account2.deposit(50).deposit(100).withdraw(20).withdraw(30).withdraw(40).withdraw(10).yield_interest().display_account_info()

# Print info of all instances of BankAccount
BankAccount.print_all_accounts_info([account1, account2])
