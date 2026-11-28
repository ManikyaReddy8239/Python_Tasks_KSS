'''Q1: 
Title: Railway_Guages 
Questions: 
Here are 5 well-structured, end-to-end scenarios (with preprocessing → analysis → 
visualization), balanced by difficulty as you requested: 
(Railway Dataset) 
�
�
**Scenario 1: Basic Data Loading & Cleaning 
You are given a CSV file containing railway gauge data. 
�
�
Tasks: 
1. Load the dataset into a Pandas DataFrame. 
2. Display the first 5 rows and column names. 
3. Check for missing values and replace them with 0. 
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types. '''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
# load dataset
df=pd.read_csv("railway_gauges.csv")
#display the first 5 rows
print("First 5 rows:")
print(df.head())
#Display the column name
print("Column Names:")
print(df.columns)
#checking missing values
print("Missing Values:")
print(df.isnull().sum())
#replace missing values with 
df=df.fillna(0)
#convert gauge columns into numeric
gauge_columns=["Broad Gauge","Metre Gauge","Narrow Gauge","Total"]
for col in gauge_columns:
    df[col]=pd.to_numeric(df[col],errors="coerce").fillna(0)
#display final data types
print("Data Types:")
print(df.dtypes)
print("Data cleaning completed")

'''�
�
Scenario 2: Simple Visualization 
You want a quick understanding of total railway track growth. 
�
�
Tasks: 
1. Extract Year and Total columns. 
2. Plot a line graph showing Total tracks over years. 
3. Add: 
○ Title 
○ X and Y labels 
4. Identify whether the trend is increasing or decreasing'''
#load database
df=pd.read_csv("railway_gauges.csv")
#Extract year and total columns
data=df[["Year","Total"]]
print("Year and Total Tracks:")
print(data)
#plot line graph
plt.figure(figsize=(12,6))
plt.plot(data["Year"],data["Total"],marker="o")
#add title and labels
plt.title("Toatl railway tracks over years")
plt.xlabel("Year")
plt.ylabel("Toatl Railway Tracks")
plt.xticks(rotation=90)
plt.grid(True)
#Save graph
plt.savefig("total_tracks_line.png")
#Display graph
plt.show()
#Identify trend
if df["Total"].iloc[-1] > df["Total"].iloc[0]:
    print("Trend: Increasing")
else:
    print("Trend: Decreasing")

'''�
�
Scenario 3: Filtering + Bar Chart 
You are asked to analyze modern railway expansion. 
�
�
Tasks: 
1. Filter the dataset for years after 2000. 
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
3. Plot a grouped bar chart comparing all three gauges. 
4. Add legend and proper labels. 
5. Identify which gauge dominates in recent years. '''

#Load dataset
df = pd.read_csv("railway_gauges.csv")
#Filter years after 2000
df["Start_Year"] = df["Year"].str[:4].astype(int)
recent_data = df[df["Start_Year"] > 2000]
#Select gauge columns
gauge_data = recent_data[
    ["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge"]]
print("Railway Data After 2000:")
print(gauge_data)
# Plot grouped bar chart
gauge_data = gauge_data.set_index("Year")
gauge_data.plot(
    kind="bar",
    figsize=(12, 6))
#Add title and labels
plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend(title="Gauge Type")
plt.xticks(rotation=45)
plt.tight_layout()
#Save graph
plt.savefig("gauge_comparison_bar.png")
# Display graph
plt.show()
# Find dominant gauge
print("\nTotal of Each Gauge After 2000:")
print(recent_data[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].sum())
print("\nBroad Gauge dominates in recent years.")

'''�
�
Scenario 4: Feature Engineering + Pie Chart 
You want to analyze the contribution of each gauge type. 
�
�
Tasks: 
1. Calculate total sum of each gauge across all years. 
2. Create a new structure (Series/DataFrame) for totals. 
3. Plot a pie chart showing percentage contribution. 
4. Add percentage labels (autopct). 
5. Interpret which gauge contributes the most. '''

# Load dataset
df = pd.read_csv("railway_gauges.csv")
#Calculate total sum of each gauge
gauge_totals = df[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].sum()
print("Total of Each Gauge:")
print(gauge_totals)
#Create DataFrame
gauge_df = pd.DataFrame({
    "Gauge": gauge_totals.index,
    "Total": gauge_totals.values})
print("\nGauge Data:")
print(gauge_df)
#Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    gauge_df["Total"],
    labels=gauge_df["Gauge"],
    autopct="%1.2f%%",
    startangle=90)
#Add title
plt.title("Percentage Contribution of Railway Gauges")
# Save graph
plt.savefig("gauge_contribution_pie.png")
# Display graph
plt.show()
# Find highest gauge
highest = gauge_totals.idxmax()
print("\nHighest Contributing Gauge:", highest)

'''�
�
Scenario 5: Advanced Analysis + Multiple Graphs 
You are asked to perform a complete analysis of railway trends. 
�
�
Tasks: 
1. Create new columns: 
○ % Broad Gauge 
○ % Metre Gauge 
○ % Narrow Gauge 
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks. 
3. Plot: 
○ Line graph for all gauges 
○ Stacked bar chart showing composition 
4. Highlight: 
○ Years with highest growth 
○ Decline in any gauge 
5. Provide a final conclusion: 
�
�
“Is the railway system shifting towards a single dominant gauge?”'''

#Load dataset
df = pd.read_csv("railway_gauges.csv")

#Create graphs folder
os.makedirs("graphs", exist_ok=True)

#Calculate percentage of each gauge
df["% Broad Gauge"] = (df["Broad Gauge"] / df["Total"]) * 100
df["% Metre Gauge"] = (df["Metre Gauge"] / df["Total"]) * 100
df["% Narrow Gauge"] = (df["Narrow Gauge"] / df["Total"]) * 100
print("Percentage Columns:")
print(df[[
    "Year",
    "% Broad Gauge",
    "% Metre Gauge",
    "% Narrow Gauge"]].round(2))
#Calculate yearly growth using NumPy
total = df["Total"].to_numpy()
growth = np.diff(total)
print("\nYearly Growth:")
print(growth)
#Find highest growth
max_growth_index = np.argmax(growth)
print("\nHighest Growth:")
print("From Year:", df["Year"].iloc[max_growth_index])
print("To Year:", df["Year"].iloc[max_growth_index + 1])
print("Growth:", growth[max_growth_index])

#Find decline in gauges
gauges = [
    "Broad Gauge",
    "Metre Gauge",
    "Narrow Gauge"]
print("\nGauge Decline Analysis:")
for col in gauges:
    if df[col].iloc[-1] < df[col].iloc[0]:
        print(col, "has decreased overall")
    else:
        print(col, "has increased overall")

#Line graph for all gauges
plt.figure(figsize=(12, 6))

plt.plot(df["Year"], df["Broad Gauge"],
         marker="o", label="Broad Gauge")

plt.plot(df["Year"], df["Metre Gauge"],
         marker="o", label="Metre Gauge")

plt.plot(df["Year"], df["Narrow Gauge"],
         marker="o", label="Narrow Gauge")

plt.title("Railway Gauge Trends Over Years")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("graphs/all_gauges_line.png")
plt.show()

#Stacked bar chart
plt.figure(figsize=(14, 7))

df.set_index("Year")[gauges].plot(
    kind="bar",
    stacked=True,
    figsize=(14, 7))

plt.title("Railway Gauge Composition")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("graphs/gauge_composition_stacked.png")
plt.show()

#Final conclusion
print("\nFinal Conclusion:")
print("Broad Gauge is the dominant railway gauge.")
print("Metre Gauge and Narrow Gauge have decreased overall.")
print("The railway system is shifting towards Broad Gauge.")
