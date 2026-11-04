#8. Write a program to find the student with the highest marks from a dictionary.
a={"Ramu":78,"Ravi":89,"Rahul":80}
b=max(a,key=a.get)
print("Students wih highest :",b, "=",a[b])
   
