'''14. Splitting Student Scores Across Servers 
A dataset: 
[50, 60, 70, 80, 90, 100, 110, 120] 
Scenario: 
A distributed system needs to divide this data among 4 servers. 
Task: 
● Convert to NumPy array. 
● Split the array into 4 equal parts using array_split().'''

import numpy as np
a=[50, 60, 70, 80, 90, 100, 110, 120]
a1=np.array(a)
print("Converted to NumPy array:",a1)
b=np.split(a1,4)
print("The array into 4 equal parts using array_split():",b)
