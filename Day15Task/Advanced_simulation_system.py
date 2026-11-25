'''10. Advanced Simulation System 
Scenario: 
Simulate exam results and generate reports. 
Task: 
● Generate random marks using random 
● Store in NumPy array 
● Convert to Pandas DataFrame 
● Use OOP to represent Student 
● Use conditions + loops to assign grades 
● Save report to file 
● Handle errors using try-except 
● Use math module for statistics'''


import random
import numpy as np
import pandas as pd
import math

# 1. Create Student class using OOP
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # 2. Assign grades using conditions
    def calculate_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 80:
            return "B"

        elif self.marks >= 70:
            return "C"

        elif self.marks >= 60:
            return "D"

        elif self.marks >= 35:
            return "E"

        else:
            return "F"

    # Check pass or fail
    def result(self):

        if self.marks >= 35:
            return "Pass"
        else:
            return "Fail"


# 3. Generate random marks
names = ["Alice", "Bob", "Charlie", "David", "Emma"]

marks = []

for name in names:
    marks.append(random.randint(0, 100))

# 4. Store marks in NumPy array
marks_array = np.array(marks)

print("Random Marks:", marks_array)


# 5. Create Student objects
students = []

for i in range(len(names)):

    student = Student(names[i], int(marks_array[i]))

    students.append(student)


# 6. Assign grades using loop
student_data = []

for student in students:

    student_data.append({
        "Name": student.name,
        "Marks": student.marks,
        "Grade": student.calculate_grade(),
        "Result": student.result()
    })


# 7. Convert into Pandas DataFrame
df = pd.DataFrame(student_data)

print("\nStudent Exam Report:")
print(df)


# 8. Calculate statistics using math module
mean_marks = math.fsum(marks) / len(marks)

variance = math.fsum(
    (mark - mean_marks) ** 2 for mark in marks
) / len(marks)

std_deviation = math.sqrt(variance)

print("\nExam Statistics:")
print("Mean Marks:", mean_marks)
print("Standard Deviation:", std_deviation)


# 9. Save report to file using exception handling
try:

    with open("exam_report.txt", "w") as file:

        file.write("STUDENT EXAM REPORT\n")
        file.write("===================\n\n")

        file.write(df.to_string())

        file.write("\n\nExam Statistics\n")
        file.write("----------------\n")

        file.write(f"Mean Marks: {mean_marks:.2f}\n")
        file.write(f"Standard Deviation: {std_deviation:.2f}\n")

    print("\nReport saved successfully!")

except PermissionError:
    print("Permission denied! Cannot save the report.")

except OSError as e:
    print("File error:", e)

except Exception as e:
    print("Unexpected error:", e)
