from company import Company 
from department import Department 
from employee import Employee


def main():
    e1 = Employee("Paul", 100, "Ingeniero")
    e2 = Employee("Ana", 120, "Diseñadora")
    
    dept1 = Department("IT")
    dept1.add_employee(e1)
    dept1.add_employee(e2)
    
    company = Company("MiEmpresa")
    company.add_department(dept1)
    
    print("Total salary:", company.total_salary())
    print("All employees:", company.all_employees())

if __name__ == "__main__":
    main()
