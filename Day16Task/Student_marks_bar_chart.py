'''2. Student Marks Bar Chart 
Scenario: 
Marks of students: 
names = ["A", "B", "C", "D"] 
marks = np.array([70, 85, 60, 90]) 
Task: 
● Create a DataFrame 
● Plot a bar graph 
● Show student names on X-axis '''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
names = ["A", "B", "C", "D"] 
marks = np.array([70, 85, 60, 90])
df=pd.DataFrame({"Names":names,"Marks":marks})
print("DataFrame:")
print(df)
plt.bar(df["Names"],df["Marks"])
plt.title("Students Marks Bar chart")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.show()
