# ~~~~~~~~~~ OOP Practice Exercises ~~~~~~~~~~ 
# Exercise 1 — Bank Accounts
"""
Create a class BankAccount with attributes: owner (string) and balance (float).
Add methods:
 - deposit(amount) → adds money to balance
 - withdraw(amount) → subtracts money if enough balance, otherwise prints "Insufficient funds"
 - get_balance() → returns current balance
 - Create two accounts and perform deposits and withdrawals. Print their balances.
"""

class BankAccount:
    def __init__(self, owner, balance = 0.0):
         self.owner = owner # public 
         self.__balance = balance # private 
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
        else:
            print("the amount must be positive")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

p1 = BankAccount("Richard", 1000)
p1.deposit(100)
p1.deposit(100)
print(p1.get_balance())
p1.withdraw(100)
print(p1.get_balance())

