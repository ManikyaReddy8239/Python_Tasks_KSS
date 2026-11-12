'''1. Armstrong Number 
Question: 
Write a program to check whether a given number is an Armstrong number or not. 
Definition: 
A number is called an Armstrong number if the sum of the cubes of its
digits is equal to the 
number itself. 
Example: 
Number = 153 
Calculation: 
1³ + 5³ + 3³ 
= 1 + 125 + 27 
= 153 
Output: 
153 is an Armstrong number'''

a=int(input("Enter a number :"))
temp=a
sum=0
while temp>0:
    digit=temp % 10
    sum=sum+digit **3
    temp=temp // 10
if sum==a:
    print(a,"is a Armstrong number")
else:
    print(a,"is not a Armstrong number")
