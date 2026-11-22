'''8.

Daily sales data: 
[200, 300, 150, 400] 
Task: 
● Store it in a NumPy array. 
● Iterate through the array and print each sale value'''

import numpy as np
a=[200, 300, 150, 400]
a1=np.array(a)
print("Stored it in a NumPy array:",a1)
print("Daily sales values:")
for i in a1:
    print(i)
