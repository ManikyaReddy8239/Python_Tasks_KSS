'''6. Matrix Transformation in Image Processing 
An image processing system stores pixel intensity values in a matrix. 
Scenario: 
[[1, 2], 
[3, 4]] 
Task: 
● Create a NumPy array for this matrix. 
● Find its transpose. 
● Print both matrices. '''

import numpy as np
a=[[1, 2],[3, 4]]
a1=np.array(a)
b=np.transpose(a1)
print("Created a Numpy array:",a1)
print("Converted into matrices:",b)
