class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

# Creating an account and performing transactions
account = BankAccount("987654321", "Julie Ann", 5000)
account.display_balance()
account.deposit(1500)
account.withdraw(3000)
account.display_balance()
