'''3. Expense Distribution Pie Chart 
Scenario: 
Monthly expenses: 
expenses = np.array([500, 300, 200]) 
labels = ["Food", "Rent", "Travel"] 
Task: 
● Create a pie chart 
● Show percentage distribution '''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
expenses = np.array([500, 300, 200]) 
labels = ["Food", "Rent", "Travel"]
df=pd.DataFrame({"Expenses":expenses,"Labels":labels})
print("Monthly expenses")
print(df)
plt.pie(expenses,labels=labels,autopct="%1.1f%%")
plt.title("Monthly expenses")
plt.show()
