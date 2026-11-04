#8. Write a program to remove duplicate values from a list using a set. 

a={2,3,5,4,8,7,6,3,2,1,6,7}
b=set()
for i in a:
    if i not in b:
        b.add(i)

print(b)
