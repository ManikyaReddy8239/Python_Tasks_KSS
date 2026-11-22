'''4. Student Roll Numbers Extraction 
A list contains roll numbers: 
[101, 102, 103, 104, 105, 106] 
Scenario: 
You want only the middle students (index 2 to 4). 
Task: 
● Use NumPy slicing to extract those values.'''

import numpy as np
a=[101, 102, 103, 104, 105, 106]
a1=np.array(a)
b=a1[2:4]
print("Slicing to extract those values:",b)
