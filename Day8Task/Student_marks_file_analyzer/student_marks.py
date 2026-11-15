'''4. Student Marks File Analyzer 
A teacher stores student marks in a file marks.txt in the format: 
Name Marks 
Example: 
Rahul 80 
Anita 90 
Ravi 75 
Write a Python program to: 
● Read the file 
● Display all student records 
● Calculate and display the average marks of the class'''

file=open("marks.txt","r")
a=file.readlines()
file.close()
print("\nStudent Records")
total=0
count=0
#display all students records
for line in a:
    name,marks=line.split()
    marks=int(marks)
    print(name,marks)
    total=total + marks
    count=count+1
if count>0:
    average=total/count
    print("\nTotal marks:",total)
    print("Average marks:",average)
else:
    print("No student records found")
