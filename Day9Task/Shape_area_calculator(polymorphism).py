'''6. Shape Area Calculator (Polymorphism) 
A graphics application needs to calculate the area of different shapes.
Create classes Circle, Rectangle, and Triangle, each having an area() method.
Demonstrate polymorphism by calling the same method for different objects.'''

import math
class Circle():
    def area(self):
        radius=5
        area=math.pi * radius * radius
        print("Area of circle:",area)
class Rectangle():
    def area(self):
        length=10
        width=5
        area=length*width
        print("Area of rectangle:",area)
class Triangle():
    def area(self):
        base=8
        height=4
        area=0.5 * base * height
        print("Area of triangle:",area)
obj=Circle()
obj1=Rectangle()
obj2=Triangle()
obj.area()
obj1.area()
obj2.area()
