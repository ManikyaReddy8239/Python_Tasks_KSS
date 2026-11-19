'''5. Vehicle Management System (Inheritance) 
A transport company manages different vehicles.
Create a base class Vehicle with attributes like brand and speed.
Create derived classes Car and Bike that inherit from 
Vehicle and display their details. '''

class vehicle():
    def __init__(self):
        self.a=str(input("Enter the vehicle brand:"))
        self.b=int(input("Enter the vehile speed:"))
    def brand(self):
        print("Vechicle brand name:",self.a)
    def speed(self):
        print("Vechicle Maximum speed:",self.b)
class car(vehicle):
    def display(self):
        print("Car details:")
        self.brand()
        self.speed()
class bike(vehicle):
    def display(self):
        print("Bike details:")
        self.brand()
        self.speed()
obj1=car()
obj1.display()
obj=bike()
obj.display()

