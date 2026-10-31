#4. Write a program that searches for a number in a list and breaks the loop when found.

a=[10,20,32,43,49]
b=int(input("Enter a number:"))
for i in a:
    if(i==b):
        print("Number is founded",i)
        break
else:
    print("Number is not found")
