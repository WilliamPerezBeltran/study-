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

# Exercise 2 — Employee & Company
"""
Create a class Employee with attributes: name and salary.
Create a class Company with attributes: name and employees (a list of Employee objects).
Add methods:
    - hire(employee) → adds an employee to the list
    - total_salary() → returns sum of all salaries
    - Practice by creating a company and 3 employees, hire them, then print total salary.
"""
class Employee: 
    def __init__(self, name, salary=0.0):
        self.name = name 
        self.salary = salary 

class Company:
    def __init__(self, name):
        self.name = name 
        self.employees = []
    
    def hire(self, employee):
        self.employees.append(employee)

    def total_salary(self):
        amount = 0.0
        for x in self.employees:
            amount += x.salary
        return amount  


e1 = Employee("william", 100)
e2 = Employee("paul", 200)
e3 = Employee("jose", 500)

c = Company("google")
c.hire(e1)
c.hire(e2)
c.hire(e3)
print(c.total_salary())

# ~~~ mejora de codigo ~~~


class Employee: 
    def __init__(self, name, salary=0.0):
        self.name = name 
        self.salary = salary
    
    def __str__(self):
        print(f"{self.name} earns {self.salary}")

class Company:
    def __init__(self, name):
        self.name = name 
        self.employees = []
    
    def hire(self, employee):
        self.employees.append(employee)

    def total_salary(self):
        return sum([x.salary for x in self.employees])
# Exercise 3 — Products & Orders

"""
Create a class Product with name and price.
Create a class Order with an attribute items (a list of Product).
Add methods:
    - add_product(product) → adds product to the order
    - total_price() → sums the prices of all products
    - Create some products, add them to an order, and print the total price.
"""
class Product():
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    def __str__(self):
        return (f"{self.name} - {self.price}")

class Order():
    def __init__(self):
        self.items = [] 

    def add_product(self,product): # adds product to the order
        return self.items.append(product)
    
    def total_price(self): # sums the prices of all products
        return sum([item.price for item in self.items])

    def __str__(self):
        if not self.items:
            return "Orders is empty"
        product_list = ", ".join(str(x.price) for x in self.items)
        return f"Order with products => {product_list}"


p1 = Product("guitar",200)
p2 = Product("piano",200)
p3 = Product("bomba",200)
c = Order()
print(c)
c.add_product(p1)
print(p1)
c.add_product(p2)
print(p2)
c.add_product(p3)
print(p3)
print(c.total_price())
print(c)
# Exercise 4 — Simple Polymorphism
"""
Create a base class Report with method generate() that prints "Generic report".
Create subclasses SalesReport and InventoryReport, each overriding generate() with a custom message.
Create a list of Report objects (some SalesReport, some InventoryReport) and loop over them calling generate().

"""

class Report():
    def generate(self):
        print("Generic report")

class SalesReport(Report):
    def generate(self):
        print("sales report")

    
class InventoryReport(Report):
    def generate(self):
        print("Inventory report")


class ReportManager():
    def __init__(self):
        self.reports = []
    
    def add_report(self, report):
        self.reports.append(report)
    
    def generate_all(self):
        return ", ".join(str(x.generate()) for x in self.reports)
            
r = ReportManager()
r.add_report(InventoryReport())
r.add_report(InventoryReport())
r.add_report(InventoryReport())
r.add_report(SalesReport())
r.add_report(SalesReport())
r.add_report(InventoryReport())
print(r.generate_all())












