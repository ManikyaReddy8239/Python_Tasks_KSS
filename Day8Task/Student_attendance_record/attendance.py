#Student Attendance Record 
#A teacher wants to store student attendance in a file named attendance.txt. Write a 
#Python program that takes a student name as input and appends it to the file. Then 
#display the contents of the file.
students_name=str(input("Enter the student name:"))
file=open("attendance.txt","a")
file.write(students_name + "\n")
file.close()
file=open("attendance.txt","r")
data=file.read()
print("\nStudent Attendance Record")
print(data)
file.close()