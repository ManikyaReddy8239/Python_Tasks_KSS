'''Then write another Python program that imports this module
and performs calculations 
based on user input. '''


#here we using import method
import Calculator
print("Addition of two number=",Calculator.add(10,20))
print("Sub of two number=",Calculator.subt(10,20))
print("Multi of two number=",Calculator.multi(10,20))
print("division of two number=",Calculator.div(10,20))

#here we using from import method
from Calculator import *
print(add(10,20))
print(subt(10,20))
print(multi(10,20))
print(div(10,20))
