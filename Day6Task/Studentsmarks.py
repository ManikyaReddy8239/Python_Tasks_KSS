'''Q1: Develop a Python program to manage student marks for three subjects. Store the subject 
names in a tuple, maintain unique student names in a set, and store each student’s marks 
in a list inside a dictionary where the key is the student name. Create user-defined 
functions to add a student with marks, display all student records, and calculate the average 
marks of a student. Implement a recursive function to calculate the total marks from the list of 
marks. The program should interact with the user through a simple menu. Also include 
exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError 
(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a 
student name entered does not exist in the dictionary). 
Example Output: 
1. Add Student 
2. Display Students 
3. Calculate Average 
4. Exit 
Enter choice: 1 
Enter student name: Rahul 
Enter marks for Math: 80 
Enter marks for Science: 85 
Enter marks for English: 90 
1. Add Student 
2. Display Students 
3. Calculate Average 
4. Exit 
Enter choice: 2 
Rahul : [80, 85, 90] 
1. Add Student 
2. Display Students 
3. Calculate Average 
4. Exit 
Enter choice: 3 
Enter student name to calculate average: Rahul 
Total Marks: 255 
Average Marks: 85.0 
1. Add Student 
2. Display Students 
3. Calculate Average 
4. Exit 
Enter choice: 4 
Example of Exception Handling Output 
ValueError 
Enter marks for Math: abc 
Invalid input! Please enter numeric marks. 
NameError 
Enter student name to calculate average: Ramesh 
Student name not found. 
ZeroDivisionError 
Cannot divide by zero. 
TypeError 
Marks data type error. '''



#Store subjects names in a tuple
subjects=("Maths","Science","English")
students=set()
student_marks={}
#FUnction 1 : Add student
def add_student():
    name=str(input("Enter the student name:"))
    if name in students:
        print("The name already exists")
        return
    marks=[]
    try:
        for subject in subjects:
            mark=int(input(f"Enter marks for {subject}:"))
            marks.append(mark)
        student_marks[name]=marks
        students.add(name)
        print("Student added successfully")
    except ValueError:
        print("Invalid input Please enter numeric marks")

#Function to display the students
def display_students():
    if not student_marks:
        print("No students records found")
    else:
        for name, marks in student_marks.items():
            print(name,":",marks)
#Recursive function to calculate total
def calculate_total(marks):
    if len(marks)==0:
        return 0
    else:
        return marks[0]+calculate_total(marks[1:])
#Function to calculate average
def calculate_average():
    name=input("Enter student name to calculate average:")
    try:
        if name not in student_marks:
            raise NameError
        marks=student_marks[name]
        if not all(isinstance(m,(int,float))for m in marks):
            raise TypeError
        total=calculate_total(marks)
        average=total/len(marks)
        print("Total marks:",total)
        print("Average marks:",average)
    except NameError:
        print("Student name not found")
    except ZeroDivisionError:
        prit("Cannot divide by zero")
    except TypeError:
        print("Marks data type error")
#Main menu

while True:
    print("\n1. Add student")
    print("2. Display students")
    print("3.Calculate Average")
    print("4.Exit")
    try:
        choice=int(input("Enter choice:"))
        if choice==1:
            add_student()
        elif choice==2:
            display_students()
        elif choice==3:
            calculate_average()
        elif choice==4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice please enter 1 to 4")
    except ValueError:
        print("Please enter a valid numeric choice")
        
