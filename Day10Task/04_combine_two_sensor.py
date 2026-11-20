'''4. Combine Two Sensor Readings 
Two sensors record readings during a test. 
Scenario: 
Sensor1 = [10, 20, 30] 
Sensor2 = [40, 50, 60] 
Task: 
● Store both readings in NumPy arrays. 
● Combine them into one array using NumPy concatenation. '''

import numpy as np
Sensor1 = [10, 20, 30] 
Sensor2 = [40, 50, 60]
a=np.array(Sensor1)
b=np.array(Sensor2)
print("Stored both readings in NumPy arrays:",(a,b))
c=np.concatenate((a,b))
print("Combined them using concatenation:",c)
