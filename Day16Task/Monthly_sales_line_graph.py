'''1. Monthly Sales Line Graph 
Scenario: 
A shop records monthly sales: 
sales = np.array([100, 150, 200, 250, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May"] 
Task: 
● Convert data into a Pandas DataFrame 
● Plot a line graph 
● Label X-axis as months and Y-axis as sales'''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
sales = np.array([100, 150, 200, 250, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May"]
df=pd.DataFrame({"months":months,"sales":sales})
print("Pandas DataFrame:")
print(df)
plt.plot(df["months"],df["sales"],marker="o")
plt.title("Monthly sales:")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
