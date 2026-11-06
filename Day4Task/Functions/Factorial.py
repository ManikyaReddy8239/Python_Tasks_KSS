#16. Write a function that returns the factorial of a number.
def  factorial(n):
    count=1
    for i in range(1,n+1):
        count=count*i
    return count
a=int(input("Enter a number ="))
res=factorial(a)
print("The factorial of a number =",res)
