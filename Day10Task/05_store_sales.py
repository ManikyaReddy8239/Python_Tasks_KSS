'''5. Store Sales Comparison 
Two stores record daily sales for 3 days. 
Scenario: 
Store A = [200, 250, 300] 
Store B = [180, 270, 310] 
Task: 
● Store them in NumPy arrays. 
● Find the daily difference in sales between the two stores. 
● Print the resulting array. '''

import numpy as np
Store1= [200, 250, 300] 
Store2= [180, 270, 310]
a=np.array(Store1)
b=np.array(Store2)
c=a-b
print("The daily difference in sales between the two stores:",c)
