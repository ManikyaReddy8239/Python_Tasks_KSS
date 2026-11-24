'''9. Missing Data Handling (NumPy + Pandas) 
A dataset: 
arr = np.array([10, np.nan, 30, np.nan, 50]) 
Task: 
● Convert to Pandas Series 
● Replace NaN values with the mean of the Series 
● Print updated data '''

import numpy as np
import pandas as pd
arr = np.array([10, np.nan, 30, np.nan, 50])
a=pd.Series(arr)
print("Pandas Series:")
print(a)
b=a.mean()
print("The mean of the series:")
print(b)
c=a.fillna(b)
print("Updated data:")
print(c)
