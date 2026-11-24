'''4. Student Marks DataFrame Analysis 
A DataFrame: 
data = pd.DataFrame({ 
"Name": ["A", "B", "C"], 
"Math": [80, 70, 60], 
"Science": [90, 60, 70] 
}) 
Task: 
● Add a new column Total = Math + Science 
● Find the student with the highest total marks'''

import numpy as np
import pandas as pd
data = pd.DataFrame({ 
                    "Name": ["A", "B", "C"], 
                    "Math": [80, 70, 60], 
                    "Science": [90, 60, 70]})
df=pd.DataFrame(data, columns=["Name","Math","Science"])
print("Original data:")
print(df)
df["Total"]=df["Math"] + df["Science"]
print("Adding a new column Total:")
print(df)
high=df.loc[df["Total"].idxmax()]
print("The student with the highest total marks:")
print("Name:",high["Name"])
print("Total marks:",high["Total"])
