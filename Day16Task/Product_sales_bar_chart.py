'''5. Product Sales Bar Chart 
Scenario: 
products = ["Pen", "Book", "Pencil"] 
sales = np.array([50, 80, 40]) 
Task: 
● Create DataFrame 
● Plot bar chart 
● Add labels and title '''


from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
products = ["Pen", "Book", "Pencil"] 
sales = np.array([50, 80, 40])
df=pd.DataFrame({"Products":products,"Sales":sales})
print("Product sales:")
print(df)
plt.bar(df["Products"],df["Sales"])
plt.title("Product Sales Bar Chart")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
