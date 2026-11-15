'''1. Write a Python program using the random module to
generate 10 random integers 
between 1 and 100 and store them in a list.
Print the list.'''

import random
b=[]
for i in range(10):
    i=random.randint(1,100)
    b.append(i)
print(b)
