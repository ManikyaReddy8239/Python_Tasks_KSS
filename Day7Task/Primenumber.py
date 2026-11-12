'''4. Prime Number 
Question: 
Write a program to check whether a number is Prime. 
Definition: 
A Prime number is a number that has only two factors: 1 and itself. 
Example: 
Number = 7 
Output: 
Factors = 1, 7 
7 is a Prime number '''


a=int(input("Enter a number:"))
count=0
for i in range(1,a+1):
    if a%i==0:
        count += 1
if count==2:
    print("Its is prime number =",a)
else:
    print("Its is not prime number =",a)
