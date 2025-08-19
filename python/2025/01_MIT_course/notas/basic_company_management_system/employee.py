from level import Level 

class Employee():
    # def __init__(self, name, salary, position, level):
    def __init__(self, name, salary, position, level):

        if not isinstance(name, str):
            raise TypeError("name must be str")

        if not isinstance(salary, int):
            raise TypeError("salary must be int")

        if not isinstance(position, str ):
            raise TypeError("Position must be str")
        
        if not isinstance(level, Level):
            raise TypeError("Level must be instance of Level ")
        self.name = name  
        self.salary = salary  
        self.position = position  
        self.level = level
        
    def __str__(self):
        return f"{self.name}-{str(self.salary)}-{self.position}-{self.level}" 
    
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

