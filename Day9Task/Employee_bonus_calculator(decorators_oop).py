'''17. Employee Bonus Calculator (Decorators & OOP) 
A company wants to apply a bonus calculation automatically before
displaying the salary.
Create an Employee class and use a decorator that
modifies the salary by 
adding a bonus before displaying it.'''

def decorator(func):
    def wrapper(self):
        bonus=self.salary*0.10
        self.salary=self.salary+bonus
        func(self)
    return wrapper
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @decorator
    def display(self):
        print("Employee Name:",self.name)
        print("Salary after bonus:",self.salary)
emp=Employee("Rakesh",30000)
emp.display()
