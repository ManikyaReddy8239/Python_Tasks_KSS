'''6. Row Selection & Deletion 
A DataFrame: 
df = pd.DataFrame({ 
"A": [10, 20, 30], 
"B": [5, 15, 25] 
}, index=["x", "y", "z"]) 
Task: 
● Select row with index "y" 
● Delete row "x" 
● Print updated DataFrame'''

import numpy as np
import pandas as pd
df = pd.DataFrame({ "A": [10, 20, 30], 
                    "B": [5, 15, 25] }, index=["x", "y", "z"])

a=df.loc['y']
print("Selected row :")
print(a)
b=df.drop('x')
print("Deleted the row X:")
print("Updated DataFrame:")
print(b)
