#18. Write a function to find the sum of elements in a list using a user-defined function.

def sum(num):
    a=0
    for i in num:
        a=a+i
    return a
b=[10,20,30]
res=sum(b)
print("Sum of all elements =",res)
