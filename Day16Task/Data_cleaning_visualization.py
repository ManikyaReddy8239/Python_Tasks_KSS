'''10. Data Cleaning + Visualization 
Scenario: 
data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
Task: 
1. Convert to Pandas Series 
2. Replace NaN with mean 
3. Plot: 
○ Line graph of cleaned data 
○ Bar chart of values > average'''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
data = np.array([100, np.nan, 200, 150, np.nan, 300])
df=pd.Series(data)
print("Pandas Series:")
print(df)
avg=df.mean()
print("Average:")
print(avg)
replace = df.fillna(avg)
print("Replaced NaN with mean:")
print(replace)
plt.figure(figsize=(10, 5))
#line graph
plt.subplot(1, 2, 1)
plt.plot(replace, marker="o", color="blue")
plt.title("Line Graph of Cleaned Data")
plt.xlabel("Index")
plt.ylabel("Values")

# 2. Bar chart of values greater than average
above_avg = replace[replace > avg]

plt.subplot(1, 2, 2)
plt.bar(above_avg.index, above_avg.values, color="green")
plt.title("Values Greater Than Average")
plt.xlabel("Index")
plt.ylabel("Values")

plt.tight_layout()
plt.show()
