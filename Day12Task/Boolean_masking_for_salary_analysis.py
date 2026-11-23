'''11. Boolean Masking for Salary Analysis 
Scenario: 
Employee salaries: 
[25000, 40000, 15000, 50000, 30000] 
Task: 
● Filter salaries above 30000. 
● Count how many employees satisfy this condition. '''

import numpy as np
a=[25000, 40000, 15000, 50000, 30000]
a1=np.array(a)
res=a1[a1>30000]
print("Salaries above 30000:",res)
count=np.sum(a1>30000)
print("Number of employees:",count)
