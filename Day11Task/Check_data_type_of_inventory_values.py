'''6. Check Data Type of Inventory Values 
A warehouse stores product quantities: 
[10, 20, 30, 40] 
Task: 
● Convert it into a NumPy array. 
● Print the data type (dtype) of the array. '''

import numpy as np
a=[10, 20, 30, 40]
a1=np.array(a)
print("Converted it into a NumPy array:",a1)
b=a1.dtype
print(b)
