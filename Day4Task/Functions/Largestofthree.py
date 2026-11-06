#20. Write a Python program with a function that returns the largest of three numbers.

def largest(a,b,c):
    if(a>b) and (a>c):
        return a
    elif(b>a) and (b>c):
        return b
    else:
        return c
a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
c=int(input("Enter the c value:"))
res=largest(a,b,c)
print("Largest number is =",res)
