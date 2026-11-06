#14. Write a program using the built-in function len() to find the length of a list.

def length():
    a=str(input("Enter any name:"))
    b=0
    for i in a:
        b=b+1
    print("The length =",b)
length()
