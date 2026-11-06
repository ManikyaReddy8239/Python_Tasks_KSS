#9. Write a program to count the frequency of each character in a string.
a="Hello everyone"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print("A program to count the frequency of each character in a string",b)
