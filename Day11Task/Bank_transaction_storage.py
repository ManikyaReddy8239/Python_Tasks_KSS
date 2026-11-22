'''1. Bank Transaction Storage 
A bank stores the transaction amounts of a customer in a list: 
[1200, 500, 800, 1500] 
Scenario: 
● Convert the list into a NumPy array. 
● Print the type of the object. 
● Verify that it is a NumPy ndarray. '''

import numpy as np
a=[1200, 500, 800, 1500]
a1=np.array(a)
print("Converted the list into a NumPy array:",a1)
b=type(a1)
print("The type of the object:",b)
print("It is a NumPy ndarray:",isinstance(a1,np.ndarray))
