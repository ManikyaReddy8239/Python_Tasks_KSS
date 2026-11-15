'''6. Employee Salary Management System 
A company stores employee data in a file employees.txt in the format: 
EmployeeName Salary 
Example: 
Ramesh 25000 
Sita 30000 
Arun 28000 
Write a Python program that: 
● Reads employee data from the file 
● Displays all employee details 
● Finds the employee with the highest salary 
● Appends a new employee record to the file.'''

file=open("employees.txt","r")
data=file.readlines()
file.close()
print("\nEmployees Details:")
highest_salary=0
highest_employee=""
#display employee details
for  line in data:
    name,salary=line.split()
    salary= int(salary)
    print(name,salary)
#find highest salary
    if salary >highest_salary:
        highest_salary=salary
        highest_employee=name
print("\nEmployee with highest salary:")
print(highest_employee,highest_salary)
#Add new employee
name=str(input("Enter a employee name:"))
salary=input("Enter employee salary:")
file=open("employees.txt","a")
file.write(name  + " " + str(salary) + "\n")
file.close()
print("New employee record added successfully")
