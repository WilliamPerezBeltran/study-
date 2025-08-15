#class

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 

    def give_raise(self, amount):
        self.salary += amount 
        print(f"{self.name} new salary: {self.salary}")

#create employee Object
emp1 = Employee("will",300)
emp2 = Employee("os",234)

print(emp1)
print(emp2)

#access atribute
print(emp1.name)

#call methods 
print(emp1.salary)
emp1.give_raise(3900)

# ~~~~~~~~~ class and instance attributes ~~~~~~~~~~

class E:
    z = "atributo classe"
    def __init__(self,x,y):
        self.x = x
        self.y = y

inst1 = E("x","y")
print(inst1.x)
print(inst1.y)
print(inst1.z)
inst1.z = "update attribute"
print(inst1.z)

# ~~~~~~~~~ Inheritance ~~~~~~~~~~

class Vehicle:
    def __init__(self,brand):
        self.brand = brand 
    
    def info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model, price):
        super().__init__(brand)
        self.model = model 
        self.price = price

    def info(self):
        print(f"model: {self.model}, model: {self.model}, price: {self.price}")

car = Car("tesla","model 3 ",3000)
car.info

# ~~~~~~~~~ polymorphism ~~~~~~~~~~
print("--")
class Report:
    def generate(self):
        print("report")

class SalesReport(Report):
    def generate(self):
        print("report sales")


class InventoryReport(Report):
    def generate(self):
        print("report inventory")

reports = [SalesReport(), InventoryReport()]

for x in reports:
    x.generate()























