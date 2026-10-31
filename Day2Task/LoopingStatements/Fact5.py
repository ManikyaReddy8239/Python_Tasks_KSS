#5. Write a program to calculate the factorial of a number using a loop.

a=int(input("enter the number:"))
fact=1
for i in range(1,a + 1):
    fact=fact*i
    print("Factorial",fact)
