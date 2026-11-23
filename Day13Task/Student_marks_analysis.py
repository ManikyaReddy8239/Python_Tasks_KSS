'''2. Student Marks Analysis 
Given marks of 5 students in 3 subjects: 
marks = np.array([ 
[70, 80, 90], 
[60, 75, 85], 
[50, 65, 70], 
[90, 95, 85], 
[40, 55, 60] 
]) 
Task: 
● Calculate total marks of each student. 
● Identify students whose total marks are above the class average'''

import numpy as np
marks = np.array([ 
[70, 80, 90], 
[60, 75, 85], 
[50, 65, 70], 
[90, 95, 85], 
[40, 55, 60]])
total=marks.sum(axis=1)
print("Total marks of each student:")
print(total)
avg=total.mean()
print("Class average:",avg)
print("Students scoring above class average:")
for i in range(len(total)):
               if total[i] > avg:
                  print("Student",i +1,":",total[i])

