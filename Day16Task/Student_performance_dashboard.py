'''1. Student Performance Dashboard 
Scenario: 
A school records marks of students in one subject: 
marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
students = ["A", "B", "C", "D", "E", "F", "G"] 
Task: 
● Convert to Pandas DataFrame 
● Plot: 
○ Line graph → trend of marks 
○ Bar chart → student vs marks 
○ Pie chart → Pass (>50) vs Fail 
○ Histogram → distribution of marks 
○ Scatter plot → index vs marks '''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
students = ["A", "B", "C", "D", "E", "F", "G"]
df=pd.DataFrame({"Marks":marks,"Students":students})
print("Students performance:")
print(df)
# Calculate Pass and Fail
passed = len(df[df["Marks"] > 50])
failed = len(df[df["Marks"] <= 50])
plt.figure(figsize=(10,5))
#Line graph
plt.subplot(3,2,1)
plt.plot(df["Students"],df["Marks"])
plt.title("Line graph → trend of marks")
plt.xlabel("Students")
plt.ylabel("Marks:")
#bar graph
plt.subplot(3,2,2)
plt.bar(df["Students"], df["Marks"])
plt.title("Bar graph")
plt.xlabel("Students")
plt.ylabel("Marks:")
#pie chart
plt.subplot(3,2,3)
plt.pie([passed,failed],labels=["Pass","Fail"],autopct="%1.1f%%")
plt.title("pie graph")
#histogram
plt.subplot(3,2,4)
plt.hist(df["Marks"], bins=5)
plt.title("Histo graph")
plt.xlabel("Marks")
plt.ylabel("No of Students")
# 5. Scatter Plot
plt.subplot(3, 2, 5)
plt.scatter(df.index, df["Marks"], color="purple")
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()
