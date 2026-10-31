#3. Write a program to find the largest of three numbers using if-elif-else.

a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
c=int(input("Enter the c value:"))
if(a>b):
    print(a, "is largest number")
elif(b>c):
    print(b, "is largest number")
else:
    print(c,"is largest number")
