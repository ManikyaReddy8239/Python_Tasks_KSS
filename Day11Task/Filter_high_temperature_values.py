'''11. Filter High Temperature Values 
A weather station records temperatures: 
[28, 31, 35, 27, 40, 22] 
Scenario: 
The system needs temperatures above 30°C. 
Task: 
● Filter the values greater than 30 using NumPy boolean filtering.'''

import numpy as np
a=[28, 31, 35, 27, 40, 22]
a1=np.array(a)
b=a1[a1 > 30]
print("The values greater than 30 using NumPy boolean filtering:",b)
