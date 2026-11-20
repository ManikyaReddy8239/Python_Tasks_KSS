'''9. Multi-Department Data Aggregation 
A company collects employee counts from two branches. 
Branch A: 
[[10, 20], 
[30, 40]] 
Branch B: 
[[5, 15], 
[25, 35]] 
Scenario: 
● Combine the two matrices. 
● Calculate the total employees across all departments. 
● Print the combined matrix and total. '''

import numpy as np
a=[[10, 20],[30, 40]]
b=[[5, 15],[25, 35]]
a1=np.array(a)
b1=np.array(b)
c=a1+b1
print("Combined the two matrices:",c)
a2=a1.sum()
b2=b1.sum()
print("The total employees across all departments:",a2+b2)
