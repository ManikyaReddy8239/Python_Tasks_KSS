#7. Write a program to remove duplicate elements from a list.
a=[2,4,3,5,8,6,2,3,6]
b=[]
for i in a:   #Checks each elements
    if i not in b:  #checka whether the elemet already exists
        b.append(i)
print(b)
