'''3. Employee Salary System (Simple Inheritance) 
A company has two types of employees: Employee and Manager.
Create a base class Employee containing name and salary.
Create a derived class Manager that inherits 
from Employee and displays the employee details. '''

class employee():
    a=str(input("Enter the employee name:"))
    b=int(input("Enter the employee salary:"))
    def name(self):
        print("Employee name:",self.a)
    def salary(self):
        print("Employee salary:",self.b)
class manager(employee):
     def display(self):
         self.name()
         self.salary()
obj=manager()
obj.display()
    

