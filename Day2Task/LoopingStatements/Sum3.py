#3. Write a program to find the sum of numbers from 1 to N using a loop.

a=int(input("Enter a number:"))
t=0
for i in range(1,a+1):
    t=t+i
    print("Sum",t)
