#5. Write a program to find the largest and smallest element in a list
a=[4,5,3,8,6,1,9]
b=max(a)
c=min(a)
print("The largest elemet is =",b ,"The smallest element is =",c)


#or else

a=[4,5,3,8,6,1,9]
a.sort()
print("Large =",a[-1],"Smallest =",a[0])
