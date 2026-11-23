'''5. Reshape & Row Averages 
A dataset: 
data = np.arange(1, 13) 
Task: 
● Reshape it into a 3×4 matrix 
● Compute average of each row'''

import numpy as np
data = np.arange(1, 13)
a=data.reshape(3,4)
print("3×4 matrix:",a)
avg=a.mean(axis=1)
print("Average of each row:",avg)
