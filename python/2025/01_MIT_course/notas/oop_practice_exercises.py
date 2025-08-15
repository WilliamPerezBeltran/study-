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
class BankAccount():
    def __init__(self,owner,balance):

