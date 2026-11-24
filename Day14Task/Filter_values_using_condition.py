'''5. Filter Values Using Condition 
A dataset: 
arr = np.array([10, 25, 30, 15, 40]) 
Task: 
● Convert to Pandas Series 
● Filter values greater than 20 '''

import numpy as np
import pandas as pd
arr = np.array([10, 25, 30, 15, 40])
pandas_series=pd.Series(arr)
print("Converted to Pandas Series:",pandas_series)
res=pandas_series[pandas_series > 20]
print("Values greater than 20:",res)
