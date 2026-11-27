'''5. Product Sales & Profit Analysis 
Scenario: 
sales = np.array([200, 300, 250, 400, 350]) 
profit = np.array([50, 70, 60, 90, 80]) 
products = ["A", "B", "C", "D", "E"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → product vs sales 
○ Pie chart → sales contribution 
○ Histogram → profit distribution 
○ Scatter plot → sales vs profit'''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
df = pd.DataFrame({
    "Products": products,
    "Sales": sales,
    "Profit": profit})
print("Product Sales & Profit Analysis:")
print(df)

plt.figure(figsize=(12, 10))

# 1. Line Graph - Sales trend
plt.subplot(3, 2, 1)
plt.plot(df["Products"], df["Sales"], marker="o", color="blue")
plt.title("Product Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")

# 2. Bar Chart - Product vs Sales
plt.subplot(3, 2, 2)
plt.bar(df["Products"], df["Sales"], color="green")
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

# 3. Pie Chart - Sales contribution
plt.subplot(3, 2, 3)
plt.pie(df["Sales"],labels=df["Products"],autopct="%1.1f%%")
plt.title("Sales Contribution")

# 4. Histogram - Profit distribution
plt.subplot(3, 2, 4)
plt.hist(df["Profit"], bins=5, color="orange", edgecolor="black")
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

# 5. Scatter Plot - Sales vs Profit
plt.subplot(3, 2, 5)
plt.scatter(df["Sales"], df["Profit"], color="purple")
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()
