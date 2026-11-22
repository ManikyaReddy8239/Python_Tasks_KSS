'''2. Device Sensor Value (Scalar Array) 
An IoT device records a single sensor reading = 75. 
Task: 
● Create a 0-D NumPy array with this value. 
● Print the value and check its number of dimensions.'''

import numpy as np
a=75
a1=np.array(a)
print("Created a 0-D NumPy array with this value:",a1)
b=a1.ndim
print("Number of dimensions:",b)
