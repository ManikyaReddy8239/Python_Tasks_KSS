'''5. Employee Management System (OOP + File + Dict) 
Scenario: 
Manage employee data. 
Task: 
● Create a class Employee 
● Store employees in a dictionary 
● Save data to a file 
● Use exception handling for invalid salary input 
● Use loop to display all employees '''

class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee ID:",self.emp_id)
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)
employees={}
try:
    n=int(input("Enter number of employees:"))
    for i in range(n):
        print("Enter Employee details")
        emp_id=input("Enter Employee ID:")
        name=input("Enter Employee Name:")
        try:
            salary=float(input("Enter Employee salary:"))
            if salary < 0:
                raise ValueError("Salary cannot be negative")
        except ValueError:
            print("Invalid Salary Please enter a valid salary")
            continue
        #Create employee object
        emp =Employee(emp_id,name,salary)
        employees[emp_id]=emp
    #display all employees
        print("Employees Records")
        for emp_id,emp in employees.items():
            print("-----------------")
            emp.display()
    #Save employees details to file
            with open("employees.txt","w") as file:
                for emp_id,emp in employees.items():
                    file.write(f"ID:{emp.emp_id},"
                               f"Name:{emp.name},"
                               f"Salary:{emp.salary},")
            print("Employee data saved sucessfully")
except ValueError:
    print("Invalid input Please enter a valid number")
except OSError as e:
    print("File error:",e)
                               
