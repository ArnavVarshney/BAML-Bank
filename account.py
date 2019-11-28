class Account:
    def __init__(self, accNo, details, balance):
        self.accNo = accNo
        self.details = details
        self.balance = balance

    def __repr(self):
        print("Account Number: ", self.accNo)
        print("Account Holder Name: ", self.details)
        print("Balance: ", self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
