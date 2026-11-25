'''6. Data Analysis Tool (NumPy + Pandas) 
Scenario: 
Analyze student marks. 
Task: 
● Generate marks using NumPy 
● Convert into Pandas DataFrame 
● Use conditions to filter passing students 
● Calculate mean using math/NumPy 
● Use loop to print results '''

import numpy as np
import pandas as pd

# 1. Generate student marks using NumPy
marks = np.array([85, 45, 90, 32, 76, 55, 28, 68])

# Student names
names = ["A", "B", "C", "D", "E", "F", "G", "H"]

# 2. Convert into Pandas DataFrame
df = pd.DataFrame({
    "Student_Name": names,
    "Marks": marks
})

print("Student Data:")
print(df)

# 3. Filter passing students (Marks >= 35)
passing_students = df[df["Marks"] >= 35]

print("\nPassing Students:")
print(passing_students)

# 4. Calculate mean using NumPy
mean_marks = np.mean(marks)

print("\nAverage Marks:", mean_marks)

# 5. Use loop to print results
print("\nStudent Results:")

for index, row in df.iterrows():
    if row["Marks"] >= 35:
        print(row["Student_Name"], "- Pass")
    else:
        print(row["Student_Name"], "- Fail")
