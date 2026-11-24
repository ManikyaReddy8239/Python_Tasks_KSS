'''7. Data Alignment Issue in Series Addition 
Two Series: 
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"]) 
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"]) 
Task: 
● Add both Series 
● Explain why some values become NaN 
● Replace NaN with 0 and compute final result'''

import numpy as np
import pandas as pd
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"]) 
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
print("Add both Series:")
a=S1+S2
print(a)
b=a.fillna(0)
print("Final Result:")
print(b)
