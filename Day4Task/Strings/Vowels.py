#6. Write a program to count the number of vowels in a string
a="Hello everyone"
b="aeiou"
count=0
for i in a:
    if i in b:
        count = count + 1
print(count)
