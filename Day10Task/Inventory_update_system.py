'''8. Inventory Update System 
A warehouse has an inventory stored in a matrix. 
[[10, 15], 
[20, 25]] 
Scenario: 
A new shipment increases every item quantity by 2 units. 
Task: 
● Add 2 to every element using NumPy. 
● Print the updated inventory.'''

import numpy as np
a=[[10, 15],[20, 25]]
a1=np.array(a)
print("original values:",a1)
b=a1+2
print("Add 2 to every element and we got updated values:",b)
