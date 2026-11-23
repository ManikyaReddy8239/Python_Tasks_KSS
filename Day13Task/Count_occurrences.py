'''7. Count Occurrences 
You have: 
data = np.array([1, 2, 2, 3, 1, 4, 2, 3]) 
Task: 
● Count how many times each unique number appears. 
● Return numbers with their counts.'''

import numpy as np
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
numbers, count = np.unique(data,return_counts=True)
print("Unique numbers:",numbers)
print("Counts:", count)
#display numbers with their counts
for num, count in zip(numbers, count):
    print(num,"appears",count,"times")
