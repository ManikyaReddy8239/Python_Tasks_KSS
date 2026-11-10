''' Write a Python program that generates 20 random numbers between 1 and 200
using the random module and store them in a list. 
Then using the math module, compute and display: 
● Maximum value 
● Minimum value 
● Square root of the maximum number 
● Logarithm of the minimum number '''

import random
import math
a=[]
for i in range(20):
    i=random.randint(1,200)
    a.append(i)
print(a)
b=max(a)
c=min(a)
print(" Maximum value=",b)
print("Minimum value=",c)
d=math.sqrt(b)
print("Square root of the maximum number=",d)
e=math.log(c)
print("Logarithm of the minimum number=",e)
