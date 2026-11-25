'''2. Random Number Analyzer 
Scenario: 
A system generates random numbers for testing. 
Task: 
● Use random to generate 10 numbers 
● Store in a list 
● Use loop + condition to count even/odd numbers 
● Use set to remove duplicates '''

import random
number=[]
for i in range(10):
    num=random.randint(1,50)
    number.append(num)
print("Generated random numbers:",number)
even=0
odd=0
for num in number:
    if num%2==0:
        even += 1
    else:
        odd += 1
print("Even numbers:",even)
print("Odd numbers:",odd)
unique=set(number)
print("Numbers without duplicates:",unique)
