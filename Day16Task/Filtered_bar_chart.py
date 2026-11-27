'''7. Filtered Bar Chart 
Scenario: 
marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"] 
Task: 
● Convert to DataFrame 
● Filter students with marks > 50 
● Plot bar chart only for filtered students'''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"]
df=pd.DataFrame({"Marks":marks,"Names":names})
print("DataFrame:")
print(df)
a=df[df["Marks"] > 50]
print("Students with marks > 50:")
print(a)
plt.bar(a["Names"],a["Marks"])
plt.title("Filtered Bar Chart")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.show()
