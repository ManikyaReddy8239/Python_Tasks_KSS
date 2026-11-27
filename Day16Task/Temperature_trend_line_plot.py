'''4. Temperature Trend Line Plot 
Scenario: 
Daily temperatures: 
temps = np.array([28, 30, 32, 31, 29]) 
Task: 
● Convert into Pandas Series 
● Plot a line graph 
● Add title and grid'''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
temps = np.array([28, 30, 32, 31, 29])
df=pd.Series(temps)
print("Daily temperatures:")
print(df)
plt.plot(df.index,df.values,marker="o")
plt.title("Daily Temperatures")
plt.xlabel("Days")
plt.ylabel("Temps")
plt.grid(True)
plt.show()
