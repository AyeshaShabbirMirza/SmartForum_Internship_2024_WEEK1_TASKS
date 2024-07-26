import pandas as pd

# LOAD THE CSV FILE
df = pd.read_csv(r'C:\Users\Me\Downloads\SampleDataSet.csv')

# CHECK FOR MISSING VALUES
missing_values = df.isnull().sum()

# DISPLAYS THE NUMBER OF MISSING VALUES
print("Number of missing values in each column:")
print(missing_values)

# TOTAL MISSING VALUES
total_missing = df.isnull().sum().sum()
print(f"\nTotal number of missing values in the DataFrame: {total_missing}")
