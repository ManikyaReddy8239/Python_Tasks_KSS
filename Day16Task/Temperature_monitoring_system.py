'''4. Temperature Monitoring System 
Scenario: 
temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → daily temperature trend 
○ Bar chart → day-wise temperature 
○ Pie chart → proportion of high (>30) vs low temps 
○ Histogram → temperature frequency 
○ Scatter plot → day index vs temperature '''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
df = pd.DataFrame({
    "Days": days,
    "Temperature": temps})
print("Temperature Monitoring System:")
print(df)

plt.figure(figsize=(12, 10))
#Line Graph
plt.subplot(3, 2, 1)
plt.plot(df["Days"], df["Temperature"], marker="o", color="blue")
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature")
#  Bar Chart
plt.subplot(3, 2, 2)
plt.bar(df["Days"], df["Temperature"], color="green")
plt.title("Day-wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
# 3. Pie Chart
high = len(df[df["Temperature"] > 30])
low = len(df[df["Temperature"] <= 30])
plt.subplot(3, 2, 3)
plt.pie([high, low],labels=["High Temperature", "Low Temperature"],autopct="%1.1f%%")
plt.title("High vs Low Temperature")
# 4. Histogram
plt.subplot(3, 2, 4)
plt.hist(df["Temperature"], bins=5, color="orange", edgecolor="black")
plt.title("Temperature Frequency")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
# 5. Scatter Plot
plt.subplot(3, 2, 5)
plt.scatter(df.index, df["Temperature"], color="purple")
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature")

plt.tight_layout()
plt.show()
