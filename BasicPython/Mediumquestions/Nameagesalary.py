'''List of Dictionaries: Given the following data:

    ```python

    employees = [

        {"name": "John", "age": 25, "salary": 30000},

        {"name": "Alice", "age": 30, "salary": 50000},

        {"name": "Bob", "age": 28, "salary": 40000},

        {"name": "David", "age": 35, "salary": 60000}

    ]

    ```

    Perform the following:

    * Find the employee with the highest salary.

    * Filter employees whose salary is greater than 35,000.

    * Calculate the average salary.

    * Create a list containing only employee names.'''
employees = [
        {"name": "John", "age": 25, "salary": 30000},
        {"name": "Alice", "age": 30, "salary": 50000},
        {"name": "Bob", "age": 28, "salary": 40000},
        {"name": "David", "age": 35, "salary": 60000}
    ]
a=max(employees, key=lambda x:x["salary"]) #lambda x represent one employee at a time
print("the highest salary ",a["name"])
for i in employees:
    if i["salary"]>35000:
        print("Salary is greater than 35000 :",i["name"],i["salary"])
total=0
for i in employees:
    total=total+i["salary"]
avg=total/len(employees)
print(avg)


names=[]
for i in employees:
    names.append(i["name"])
print(names)
