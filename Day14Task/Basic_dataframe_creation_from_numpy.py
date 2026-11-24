'''2. Basic DataFrame Creation from NumPy 
You have: 
data = np.array([[1, 2], [3, 4], [5, 6]]) 
Task: 
● Convert it into a Pandas DataFrame 
● Add column names: "X", "Y" '''

import numpy as np
import pandas as pd
data = np.array([[1, 2], [3, 4], [5, 6]])
series=pd.DataFrame(data, columns=["X","Y"])
print("Converted it into a Pandas DataFrame:")
print(series)
