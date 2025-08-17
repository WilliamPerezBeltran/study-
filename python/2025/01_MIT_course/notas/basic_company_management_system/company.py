class Company():
    def __init__(self, name):
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
        













