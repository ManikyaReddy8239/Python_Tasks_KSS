#5. Write a program to assign grades based on marks (for example: A, B, C, Fail)
a=int(input("Enter the marks:"))
if(a>90):
    print(a,"Grade is A")
elif(a>80):
    print(a,"Grade is B")
elif(a>70):
    print(a,"Grade is C")
elif(a>50):
    print(a,"Grade is D")
else:
    print(a,"Its is fail")
