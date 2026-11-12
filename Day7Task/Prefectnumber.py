'''5. Perfect Number 
Question: 
Write a program to check whether a number is a Perfect number. 
Definition: 
A Perfect number is a number whose sum of proper divisors equals the number. 
Example: 
Number = 6 
Divisors: 1, 2, 3 
Sum = 1 + 2 + 3 = 6 
Output: 
6 is a Perfect number'''


a=int(input("Enter a number:"))
sum=0
for i in range(1,a):
    if a % i == 0:
        sum=sum+i
if sum==a:
    print(a,"is perfect number")
else:
    print(a,"is not perfect number")
