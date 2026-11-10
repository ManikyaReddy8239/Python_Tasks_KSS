'''* Dictionary Sorting: Given a dictionary:
 
    ```python
    students = {
        "Rahul": 85,
        "Amit": 92,
        "Priya": 78,
        "Sneha": 95
    }
    ```
 
Sort the dictionary based on marks in descending order and print
the top two students.'''

students = {"Rahul": 85,"Amit": 92,"Priya": 78,"Sneha": 95}
sorted_students=sorted(students.items(),key=lambda x: x[1],reverse=True)
'''sorted() Sorts the data
students.items() Gets names and marks
key=lambda x: x[1] Sorts using marks
reverse=True Highest to lowest'''
print("Sorted students :",sorted_students)
print("Top two students:")
for i in sorted_students[:2]:
    print(i[0],i[1])


'''sorted()=arrange in order
reverse=True=Highest to lowest
[:2]=Get first two values
[0]=Name
[1]=Marks'''
