'''3. Employee Data Copy Issue (Shallow vs Deep Copy) 
A company stores employee data: 
employees = [[101, "A"], [102, "B"], [103, "C"]] 
Scenario: 
● Create a shallow copy of the list. 
● Modify one nested list (e.g., change "A" to "Z"). 
● Observe changes in both lists. 
Task: 
● Explain why the change reflects in both. 
● Fix it using deep copy.'''


import copy
employees = [[101, "A"], [102, "B"], [103, "C"]]
#create shallow copy
shallow_copy=copy.copy(employees)
print("Original list:",employees)
print("Shallow copy:",shallow_copy)
#Modify nested list
employees[0][1]="Z"
print("Original list:",employees)
print("Deep copy:",shallow_copy)

deep_copy=copy.deepcopy(employees)
print("Original list:",employees)
print("Deep copy:",deep_copy)
#Modify nested list
employees[1][1]="X"
print("Original list:",employees)
print("Deep copy:",deep_copy)
