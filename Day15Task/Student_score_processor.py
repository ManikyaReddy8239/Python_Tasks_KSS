'''1. Student Score Processor 
Scenario: 
A teacher stores student names and marks in a list of tuples. 
Task: 
● Convert data into a dictionary 
● Use a loop + condition to find students scoring above 50 
● Use math module to calculate average 
● Store results in a text file '''

import math
students=[("Rahul",85),("Priya",45),("Raju",75),("Ravi",83),("Radha",35)]
#Covertind list into a dictionary
student_dict=dict(students)
print("Students Recorded:")
print(student_dict)
#finding the students above 50
print("Students scoring above 50:")
above=[]
for name,marks in student_dict.items():
    if marks > 50:
        above.append((name,marks))
        print(name,":",marks)
#clculate the average
total=math.fsum(student_dict.values())
average=total/len(student_dict)
print("Average marks:")
print(average)
#text file
with open("students_result.txt","w") as file:
    
    file.write("Students score processor:")
    file.write("------------------------")
    file.write("Student records:")
    for name,marks in student_dict.items():
       file.write(f"{name}:{marks}\n")
    file.write("Students scoring above 50:")
    for name,marks in above:
        file.write(f"{name}:{marks}\n")
    file.write("Average marks:{average}")
print("Results saved successfully in students_result,txt")
