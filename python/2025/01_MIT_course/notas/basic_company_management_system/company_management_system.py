# company management system 
"""
Classes & Relationships
 Employee
    - Attributes: name (str), salary (float), position (str),level 
    - Methods: give_raise(amount), promote(new_position)
 Department
    - Attributes: name (str), employees (list of Employee objects)
    - Methods: add_employee(employee), department_salary(), list_employees()
 Company
    - Attributes: name (str), departments (list of Department objects)
    - Methods: add_department(dept), total_salary(), all_employees()


- Regarding promotion and new position 
    Nivel Operativo
        - Practicante / Intern
        - Asistente / Junior Analyst / Junior Developer
        - Analista / Developer / Ingeniero de Soporte

    Nivel Intermedio
        - Senior Analyst / Senior Developer
        - Líder Técnico / Team Lead
        - Coordinador / Supervisor / Project Manager

    Nivel Estratégico / Ejecutivo
        - Gerente (Manager)
        - Director (Head of / Director)
        - Vicepresidente (VP)
"""
class Employee():
    def __init__(self, name, salary, position, level):
        self.name = name  
        self.salary = salary  
        self.position = position  
    
    def give_raise(self, amount):
        try:
            if amount > 0:
                self.salary += amount 
        except Exception as e:
            print("Error: ", e)

    def promote(self, new_position):
        try:
            self.position = new_position 
        except Exception as e:
            print("Error in promote: ", e)

class Department():
    def __init__(self, name):
        self.name = name  
        self.employees = [] # (list of Employee objects)
    
    def add_employee(self, employee):
        try:
            self.employees.append(employee) 
        except Exception as e:
            print("Error: ", e)

    def department_salary(self):
        try:
            return sum([employee.salary for employee in  self.employees])
        except Exception as e:
            print("Error in department_salary: ", e)

    def list_employees(self):
        try:
            ", ".join(employee.name for employee in self.employees)
        except Exception as e:
            print("Error in list_employees: ", e)



class Company():
    def __init__(self, name, departments):
        self.name = name  
        self.departments = []   
    
    def add_department(self, dept): # list of Department objects
        try:
            self.departments.append(dept)
        except Exception as e:
            print("Error in add_department: ", e)
        

    def total_salary(self):
        try:
             #for department in self.departments:
                #for x in department.employees:
                    #print(x.salary)

            return sum([x.salary for department in self.departments for x in department.employees])

            #return sum([x.salary for x in self.departments])
        except Exception as e:
            print("Error in add_department: ", e)


    def all_employees(self):
        try:
            return "- ".join([str(x.name) for department in self.departments for x in department.employees])
        except Exception as e:
            print("Error in all_employees: ", e)
        













