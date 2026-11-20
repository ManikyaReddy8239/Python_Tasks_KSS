'''3. Sorting Product Prices 
An e-commerce company stores product prices in a NumPy array. 
Scenario: 
Prices = [499, 299, 799, 199, 599] 
Task: 
● Convert it into a NumPy array. 
● Sort the prices in ascending order.'''

import numpy as np
a=[499, 299, 799, 199, 599]
a1=np.array(a)
print("Converting list into Numpy:",a1)
b=np.sort(a1)
print("The prices in ascending order:",b)
