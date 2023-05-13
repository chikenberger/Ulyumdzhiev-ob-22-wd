class BankAccount:
    def __init__(self, ownerName, number, balance):
        self.ownerName = ownerName
        self.number = number
        self.balance = balance

    def withdrawMoney(self, quantity):
        self.balance -= quantity
        return self

    def addMoney(self, quantity):
        self.balance += quantity
        return self
