class Employee():
    # def __init__(self, name, salary, position, level):
    def __init__(self, name, salary, position):
        self.name = name  
        self.salary = salary  
        self.position = position  
        
    def __str__(self):
        return f"{self.name}-{str(self.salary)}-{self.position}" 
    
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

