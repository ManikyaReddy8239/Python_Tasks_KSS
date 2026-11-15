#The main program code here

from Utilities.Math_operations import *
from Utilities.String_operations import *
a=int(input("Enter a number :"))
b=int(input("Enter b number :"))
print("Addition of two numbers=",add(a,b))
print("Multiplication of two numbers=",multi(a,b))
text=str(input("Enter a string:"))
print("To covert string into uppercase",uppercase(text))
print("To count characters in a string:",count(text))
