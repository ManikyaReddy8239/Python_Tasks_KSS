'''9. Combined Visualization Dashboard 
Scenario: 
sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph (trend) 
○ Bar chart (comparison) 
○ Pie chart (distribution) 
● Show all in single figure (subplots) '''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"]
df=pd.DataFrame({"Products":products,"Sales":sales,})
print("DataFrame:")
print(df)
plt.figure(figsize=(15,5))
plt.subplot(2,2,1)
plt.plot(df["Products"],df["Sales"])
plt.title("Products Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.subplot(2,2,2)
plt.bar(df["Products"],df["Sales"])
plt.title("Products Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.subplot(2,2,3)
plt.pie(df["Sales"],labels=df["Products"],autopct="%1.1f%%")
plt.title("Products Sales")
plt.tight_layout() #Adjusts spacing between graphs
plt.show()
