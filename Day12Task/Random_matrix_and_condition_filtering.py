'''10. Random Matrix and Condition Filtering 
Scenario: 
● Generate a 3×3 matrix of random numbers (0–50). 
Task: 
● Filter elements greater than 25. 
● Print filtered values. '''

import numpy as np
a=np.random.randint(0,51,(3,3))
print("Original martix:",a)
res=a[a>25]
print("Filtered values:",res)
