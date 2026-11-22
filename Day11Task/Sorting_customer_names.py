'''12. Sorting Customer Names
A system stores customer names: 
["Ravi", "Anil", "Sita", "John"] 
Task: 
● Convert it to a NumPy array. 
● Sort the names alphabetically.'''

import numpy as np
names=["Ravi", "Anil", "Sita", "John"]
a=np.array(names)
print("Converted it to a NumPy array:",a)
b=np.sort(a)
print("Sorted the names alphabetically:",b)
