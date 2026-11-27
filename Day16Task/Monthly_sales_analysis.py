'''2. Monthly Sales Analysis 
Scenario: 
sales = np.array([100, 150, 200, 180, 220, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → month-wise comparison 
○ Pie chart → contribution of each month 
○ Histogram → frequency of sales values 
○ Scatter plot → month index vs sales'''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
sales = np.array([100, 150, 200, 180, 220, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df=pd.DataFrame({"Months":months,"Sales":sales})
print("Monthly sales:")
print(df)
plt.figure(figsize=(10,9))
#line
plt.subplot(3,2,1)
plt.plot(df["Months"], df["Sales"])
plt.title("Line graph → sales trend")
plt.xlabel("Months")
plt.ylabel("Sales")
#Bar chart
plt.subplot(3,2,2)
plt.bar(df["Months"], df["Sales"])
plt.title("Bar chart")
plt.xlabel("Months")
plt.ylabel("Sales")
#Pie chart
plt.subplot(3,2,3)
plt.pie(df["Sales"], labels=df["Months"], autopct="%1.1f%%")
plt.title("Pie chart")
#Histogram
plt.subplot(3,2,4)
plt.hist(df["Sales"],bins=5)
plt.title("Histo graph")
plt.xlabel("Sales")
plt.ylabel("Frequency")
#Scatter
plt.subplot(3,2,5)
plt.scatter(df.index,df["Sales"])
plt.title("Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
