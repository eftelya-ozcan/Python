class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if (amount > 0):
            self.balance -= amount
            print(f"Withdrew: ${amount}, New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if (amount > 0 and amount <= self.balance):
            self.balance =- amount
            print(f"Withdrew: ${amount}, New Balance: ${self.balance}")
        elif(amount > self.balance):
            print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest Added: ${interest}, New Balance: ${self.balance}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if (amount > 0 and amount <= self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew: ${amount}, New Balance: ${self.balance}")
        elif (amount > self.balance + self.overdraft_limit):
            print("Overdraft limit exceeded")
        else:
            print;("Withdrawal amount must be positive")


class BusinessAccount(BankAccount):
    def __init__(self, account_number, balance=0, credit_line=0):
        super().__init__(account_number, balance)
        self.credit_line = credit_line

    def withdraw(self, amount):
        available_funds = self.balance + self.credit_line
        if (amount > 0 and amount <= available_funds):
            self.balance -= amount
            print(f"Withdrew: ${amount}, New Balance: ${self.balance}")
        elif (amount > available_funds):
            print("Credit line limit exceeded")
        else:
            print("Withdrawal amount must be positive.")

    def request_loan(self, amount):
        print(f"Loan request of ${amount} has been submitted for review.")


# Creating objects for each account type
savings = SavingsAccount("SA12345", 1000, 0.02)
checking = CheckingAccount("CA67890", 500, 200)
business = BusinessAccount("BA11223", 2000, 5000)

# Performing operations on each account
print("Savings Account Operations:")
savings.display_balance()
savings.deposit(500)
savings.add_interest()
savings.withdraw(200)

print("\nChecking Account Operations:")
checking.display_balance()
checking.deposit(300)
checking.withdraw(1000)  # Within overdraft limit
checking.withdraw(800)   # Exceeds overdraft limit

print("\nBusiness Account Operations:")
business.display_balance()
business.deposit(1000)
business.withdraw(4000)  # Within credit line
business.request_loan(10000)
