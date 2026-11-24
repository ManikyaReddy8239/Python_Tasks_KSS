'''4. Find Maximum Value 
A dataset: 
arr = np.array([12, 45, 22, 67, 34]) 
Task: 
● Convert to Pandas Series 
● Find the maximum value'''

import numpy as np
import pandas as pd
arr = np.array([12, 45, 22, 67, 34])
pandas_series=pd.Series(arr)
print("Converted into Pandas series:",pandas_series)
b=pandas_series.max()
print("The maximum value:",b)
