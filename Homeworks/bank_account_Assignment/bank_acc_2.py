from bank_acc_1 import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {} 

    def add_account(self, account_name, interest_rate=0.02, balance=0):
        self.accounts[account_name] = BankAccount(interest_rate, balance)

    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print("Account not found")

    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print("Account not found")

    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            print(f"User: {self.name}, Account: {account_name}")
            self.accounts[account_name].display_account_info()
        else:
            print("Account not found")

    def transfer_money(self, amount, other_user, from_account, to_account):
        if from_account in self.accounts and to_account in other_user.accounts:
            if self.accounts[from_account].balance >= amount:
                self.accounts[from_account].withdraw(amount)
                other_user.accounts[to_account].deposit(amount)
                print(f"${amount} transferred from {self.name}'s {from_account} to {other_user.name}'s {to_account}")
            else:
                print("Insufficient funds")
        else:
            print("One or both accounts not found")


# usage
user1 = User("mari", "mari@gmail.com")
user1.add_account("Savings")
user1.add_account("Checking", interest_rate=0.01, balance=500)

user2 = User("nazuk", "nazuk@gmail.com")
user2.add_account("Savings")

# Make deposit
user1.make_deposit("Savings", 1000)
user1.make_deposit("Checking", 500)

# Make withdrawal
user1.make_withdrawal("Checking", 200)

# Display user balance
user1.display_user_balance("Savings")
user1.display_user_balance("Checking")

# Transfer money
user1.transfer_money(300, user2, "Checking", "Savings")

# Display user balances after transfer
user1.display_user_balance("Savings")
user2.display_user_balance("Savings")
