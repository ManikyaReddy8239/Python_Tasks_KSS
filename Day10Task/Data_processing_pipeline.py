'''10. Data Processing Pipeline 
A data pipeline receives the following array: 
[12, 7, 25, 3, 18, 10] 
Scenario: 
1. Convert the list into a NumPy array. 
2. Sort the array. 
3. Split the sorted array into two equal parts. 
4. Calculate the sum of each part. 
Output: 
● Sorted array 
● Two split arrays 
● Sum of each part'''

import numpy as np
a=[12, 7, 25, 3, 18, 10]
a1=np.array(a)
a2=np.sort(a1)
print("Sorted the array:",a2)
a3=np.split(a2,2)
print("The sorted array into two equal parts:",a3)
a4=[arr.sum() for arr in a3]  #Takes each array one by ine Calculates the sum pf that array
print("The sum of each part:",a4)
