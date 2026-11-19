'''1. Student Information System (Class & Object) 
A school wants a program to store student details.
Create a Student class with 
attributes such as name, roll number, and marks.
Create objects for at least three 
students and display their details. '''

class student():
    name="Mani"
    roll_number=11
    marks=70
    def display(self):
        print("To store student details:")
        print("Student name:",self.name)
        print("Student roll number:",self.roll_number)
        print("Student marks:",self.marks)
obj=student()
obj.display()

obj2=student()
obj2.name="rahul"
obj2.roll_number=9
obj2.marks=78
obj2.display()

obj3=student()
obj3.name="raju"
obj3.roll_number=10
obj3.marks=72
obj3.display()
