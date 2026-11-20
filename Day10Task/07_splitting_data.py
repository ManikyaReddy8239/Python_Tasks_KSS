'''7. Splitting Data for Parallel Processing 
A dataset contains the following values: 
[5, 10, 15, 20, 25, 30] 
Scenario: 
You want to distribute the data across 3 processors. 
Task: 
● Store the data in a NumPy array. 
● Split it into 3 equal parts using NumPy.'''

import numpy as np
a=[5, 10, 15, 20, 25, 30]
a1=np.array(a)
print("Stored the data in a NumPy array:",a1)
b=np.split(a1,3)
print("Splited it into 3 equal parts:",b)
