class Department():
    def __init__(self, name):
        self.name = name  
        self.employees = [] # (list of Employee objects)
    
    def add_employee(self, employee):
        try:
            return self.employees.append(employee) 
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

