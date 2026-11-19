'''10. University Staff Management (Hierarchical Inheritance) 
A university has different staff types such as Professor, LabAssistant, and 
Administrator.
All inherit from a base class Staff. Implement hierarchical inheritance 
to manage and display their information. '''

class Staff:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Professor(Staff):
    def __init__(self,name,age,subject):
        self.name=name
        self.age=age
        self.subject=subject
    def show(self):
        self.display()
        print("Subject:",self.subject)
class LabAssistant(Staff):
    def __init__(self,name,age,lab):
        self.name=name
        self.age=age
        self.lab=lab
    def show(self):
        self.display()
        print("Lab:",self.lab)
class Administrator(Staff):
    def __init__(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department
    def show(self):
        self.display()
        print("Department:",self.department)
p=Professor("Rakesh",45,"Python")
l=LabAssistant("Rahul",34,"Computerlab")
a=Administrator("Admit",40,"Management")
print("Professor Details:")
p.show()
print("\nLab Assistant:")
l.show()
print("\nAdministrator:")
a.show()
