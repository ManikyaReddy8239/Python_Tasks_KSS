'''6. Multi-Line Graph for Sales Comparison 
Scenario: 
data = { 
"Month": ["Jan", "Feb", "Mar"], 
"Store_A": [100, 150, 200], 
"Store_B": [90, 140, 210] 
} 
Task: 
● Create DataFrame 
● Plot two line graphs on same plot 
● Add legend '''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
data = { 
        "Month": ["Jan", "Feb", "Mar"], 
        "Store_A": [100, 150, 200], 
        "Store_B": [90, 140, 210]}
df=pd.DataFrame(data)
print("Created DataFrame:")
print(df)
plt.plot(df["Month"],df["Store_A"],marker="o",label="Store A")
plt.plot(df["Month"],df["Store_B"],marker="o",label="Store B")
plt.title("Sales Comparsion")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()
