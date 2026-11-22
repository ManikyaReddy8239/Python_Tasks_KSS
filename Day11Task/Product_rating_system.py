'''3. Product Rating System 
An e-commerce website stores product ratings: 
[4, 5, 3, 4, 2] 
Task: 
● Convert it to a NumPy array. 
● Print the first and last rating using indexing. '''

import numpy as np
a=[4, 5, 3, 4, 2]
a1=np.array(a)
print("Converted it to a NumPy array:",a1)
b=a[0]
print("First rating is:", b)
c=a[-1]
print("Last rating is:",c)
