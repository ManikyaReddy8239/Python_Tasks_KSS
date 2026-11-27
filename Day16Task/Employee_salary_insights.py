'''3. Employee Salary Insights 
Scenario: 
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
Task: 
● Convert into DataFrame 
● Plot: 
○ Line graph → salary trend 
○ Bar chart → department-wise salary comparison 
○ Pie chart → department distribution 
○ Histogram → salary distribution 
○ Scatter plot → index vs salary '''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
df=pd.DataFrame({"Departments":departments,"Salaries":salaries})
print("Employee Salary Insights:")
print(df)
plt.figure(figsize=(10,9))
#line
plt.subplot(3,2,1)
plt.plot(df.index, df["Salaries"], marker="o")
plt.title("Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
#bar
dept_salary = df.groupby("Departments")["Salaries"].mean()

plt.subplot(3,2,2)
plt.bar(dept_salary.index, dept_salary.values)
plt.title("Department-wise Average Salary")
plt.xlabel("Departments")
plt.ylabel("Average Salary")
#pie
plt.subplot(3,2,3)
dept_count = df["Departments"].value_counts()
plt.pie(dept_count, labels=dept_count.index, autopct="%1.1f%%")
plt.title("Pie graph")
#hist
plt.subplot(3,2,4)
plt.hist(df["Salaries"], bins=5, edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salaries")
plt.ylabel("Frequency")
#scatter
plt.subplot(3,2,5)
plt.scatter(df.index, df["Salaries"])
plt.title("Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()
