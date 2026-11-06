#10. Write a program to remove duplicate characters from a string.
a="Hello everyone"
b=""
for i in a:
    if i not in b:
        b+=i
print(b)
