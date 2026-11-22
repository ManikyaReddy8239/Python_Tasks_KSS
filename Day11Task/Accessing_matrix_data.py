'''5. Accessing Matrix Data 
A teacher stores marks of students in two subjects: 
[[78, 85], 
[90, 88], 
[67, 72]] 
Task: 
● Convert it to a NumPy array. 
● Access the second student's second subject mark.'''

import numpy as np
a=[[78, 85],[90, 88],[67, 72]]
a1=np.array(a)
print("Converted it to a NumPy array:",a1)
b=a1[1,1]
print("The second student's second subject mark:",b)
