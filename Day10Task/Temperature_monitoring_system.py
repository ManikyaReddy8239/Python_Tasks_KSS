'''2. Temperature Monitoring System 
A weather station records temperatures for two days. 
Scenario: 
Day 1: [30, 32, 31] 
Day 2: [29, 33, 34] 
Task: 
● Create a 2D NumPy array to store this data. 
● Print the array. 
● Find the total temperature recorded.'''

import numpy as np
a=[30, 32, 31] 
b=[29, 33, 34]
a1=np.array(a)
b1=np.array(b)
c=np.array([a,b])
print("A 2D NumPy array to store this data:",c)
d=a1.sum()
e=b1.sum()
print("The total temperature recorded:",d+e)
