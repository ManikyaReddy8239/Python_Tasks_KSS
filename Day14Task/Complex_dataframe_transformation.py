'''8. Complex DataFrame Transformation 
A DataFrame: 
df = pd.DataFrame({ 
"Name": ["A", "B", "C", "D"], 
"Marks": [50, 80, 30, 90] 
}) 
Scenario: 
● Students scoring below 50 failed 
Task: 
1. Create a column Status ("Pass"/"Fail") 
2. Filter only passed students 
3. Calculate average marks of passed students'''

import numpy as np
import pandas as pd
df = pd.DataFrame({ 
"Name": ["A", "B", "C", "D"], 
"Marks": [50, 80, 30, 90]})
print("Original DataFrame:")
print(df)
#creating pass/fail status column
df["Status"]=df["Marks"].apply(lambda x : "Pass" if x >= 50 else "Fail")
print("DataFrame with Pass/fail status:")
print(df)
#filter only passed students
passed=df[df["Status"] == "Pass"]
print("Passed students:")
print(passed)
avg=passed["Marks"].mean()
print("Average marks of passed students:")
print(avg)
