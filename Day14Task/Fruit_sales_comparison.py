'''1. Fruit Sales Comparison (Series Addition) 
A shop tracks fruit sales: 
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"]) 
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"]) 
Task: 
● Add both series 
● Find the total sales of all fruits combined'''

import numpy as np
import pandas as pd
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"]) 
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
add=S1 + S2
print("Added both Series:")
print(add)
max_fruits=add.sum()
print("The total sales of all fruits combined:")
print(max_fruits)
