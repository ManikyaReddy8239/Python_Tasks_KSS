'''7. Convert Float Prices to Integer 
A shop stores product prices: 
[10.5, 20.8, 15.3] 
Scenario: 
The billing system requires integer values. 
Task: 
● Convert the array from float to integer using astype().'''

import numpy as np
a=[10.5, 20.8, 15.3]
a1=np.array(a)
print("The original array:",a1)
b=a1.astype(int)
print("Converted the array from float to integer:",b)
