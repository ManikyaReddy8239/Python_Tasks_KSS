'''10. Find Indexes of Specific Value 
A quality check system stores product defect codes: 
[2, 4, 1, 4, 3, 4, 5] 
Task: 
● Find the indexes where value = 4 using NumPy searching.'''

import numpy as np
a=[2, 4, 1, 4, 3, 4, 5]
a1=np.array(a)
b=np.where(a1==4)
print("The indexes where value = 4 using NumPy searching:",b)
