'''13. Copy vs View Behavior in Data Processing 
Scenario: 
A dataset: 
[10, 20, 30, 40] 
Task: 
● Create a copy of the array. 
● Modify the original array. 
● Show that the copy does not change. 
● Repeat using view() and observe the difference. '''

import numpy as np

a = [10, 20, 30, 40]
a1 = np.array(a)

# Creating a copy
b = a1.copy()

# Modifying original array
a1[0] = 100

print("Original Array:", a1)
print("Copied Array:", b)

# Creating a view
c = a1.view()

# Modifying original array again
a1[1] = 200

print("Original Array:", a1)
print("View Array:", c)
