#1. Write a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
a=int(input("Enter a number :"))
res=factorial(a)
print("The factorial of a number =",res)
