'''8. Pie Chart with Conditional Data 
Scenario: 
scores = np.array([40, 60, 80, 30, 90]) 
Task: 
● Categorize into: 
○ Pass (>50) 
○ Fail (<=50) 
● Count using NumPy/Pandas 
● Plot pie chart for Pass vs Fail 
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
scores = np.array([40, 60, 80, 30, 90])
result=[]
for i in scores:
    if i > 50:
        result.append("Pass")
    else:
        result.append("Fail")
df=pd.DataFrame({"Scores":scores,"Result":result})
print("Student Results:")
print(df)
counts=df["Result"].value_counts()
print("Pass and Fail Count:")
print(counts)
plt.pie(counts,labels=counts.index,autopct="%1.1f%%")
plt.title("Pass and fail Distribution")
plt.show()
