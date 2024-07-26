import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1. CREATING SERIES
print("\n1. CREATING SERIES")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("SERIES S:\n", s)

#2. CREATING DATAFRAME
print("\n2. CREATING DATAFRAME")
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': ['FOO', 'BAR', 'BAZ', 'QUX']
})
print("DATAFRAME DF: \n", df)

#3. READING CSV FILE
print("\n3. READING CSV FILE")
df_csv = pd.read_csv(r'C:\Users\Me\Downloads\employees.csv')
print("DATAFRAME FROM CSV:\n", df_csv.head())

#4. READING JSON FILE
print("\n4. READING JSON FILE")
df_json = pd.read_json(r'C:\Users\Me\Downloads\employees.json')
print("DATAFRAME FROM JSON: \n", df_json)

#5. ANALYZE DATA
print("\n5. ANALYZE DATA")
print("DESCRIPTIVE STATISTICS OF DF: \n", df.describe())

#6. ACCESSING ROWS
print("\n6. ACCESSING ROWS")
print("FIRST ROW OF DF: \n", df.iloc[0])

#7. ACCESSING COLUMNS
print("\n7. ACCESSING COLUMNS")
print("COLUMN 'A' OF DF: \n", df['A'])

#8. ACCESSING ELEMENTS
print("\n8. ACCESSING ELEMENTS")
print("ELEMENT AT [0, 'A'] IN DF: ", df.at[0, 'A'])

#9. MODIFYING ELEMENTS
print("\n9. MODIFYING ELEMENTS")
df.at[0, 'A'] = 10
print("DATAFRAME DF AFTER MODIFYING ELEMENT: \n", df)

#10. ADDING ROWS
print("\n10. ADDING ROWS")
df = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4],
    'C': ['FOO', 'BAR']
})
new_row = pd.DataFrame([{'A': 5, 'B': 9, 'C': 'QUUX'}])
df = pd.concat([df, new_row], ignore_index=True)
print("DATAFRAME DF AFTER ADDING ROW: \n", df)

#11. ADDING COLUMNS
print("\n11. ADDING COLUMNS")
df['D'] = df['A'] + df['B']
print("DATAFRAME DF AFTER ADDING COLUMN 'D': \n", df)

#12. REMOVING ROWS
print("\n12. REMOVING ROWS")
df = df.drop(index=[0])
print("DATAFRAME DF AFTER REMOVING ROW: \n", df)

#13. REMOVING COLUMNS
print("\n13. REMOVING COLUMNS")
df = df.drop(columns=['D'])
print("DATAFRAME DF AFTER REMOVING COLUMN 'D': \n", df)

#14. CLEANING EMPTY CELLS
print("\n14. CLEANING EMPTY CELLS")
df.at[1, 'B'] = np.nan
print("DATAFRAME DF WITH NAN: \n", df)
print("DATAFRAME DF AFTER FILLING NAN WITH 0: \n", df.fillna(0))

#15. CLEANING WRONG FORMAT
print("\n15. CLEANING WRONG FORMAT")
df.at[2, 'C'] = 123
print("DATAFRAME DF WITH WRONG FORMAT: \n", df)
df['C'] = df['C'].astype(str)
print("DATAFRAME DF AFTER CONVERTING 'C' TO STRING: \n", df)

#16. CLEANING WRONG DATA
print("\n16. CLEANING WRONG DATA")
df.at[3, 'A'] = -1
print("DATAFRAME DF WITH WRONG DATA: \n", df)
df.loc[df['A'] < 0, 'A'] = np.nan
print("DATAFRAME DF AFTER CLEANING WRONG DATA: \n", df)

#17. REMOVING DUPLICATES
print("\n17. REMOVING DUPLICATES")
df = pd.DataFrame({
    'A': [1, 2, 3, 1],
    'B': [4, 5, 6, 4],
    'C': ['X', 'Y', 'Z', 'X']
})
df = df.drop_duplicates()
print("DATAFRAME DF AFTER REMOVING DUPLICATES: \n", df)

#18. CORRELATIONS
print("\n18. CORRELATIONS")
numeric_df = df.select_dtypes(include='number')
correlation_matrix = numeric_df.corr()
print("CORRELATION BETWEEN NUMERIC COLUMNS IN DF: \n", correlation_matrix)

#19. TIME SERIES ANALYSIS
print("\n19. TIME SERIES ANALYSIS")
date_rng = pd.date_range(start='2024-07-22', end='2024-08-01', freq='D')
df_time = pd.DataFrame(date_rng, columns=['DATE'])
df_time['DATA'] = np.random.randint(0, 100, size=(len(date_rng)))
df_time = df_time.set_index('DATE')
print("TIME SERIES DATAFRAME DF_TIME: \n", df_time)

#20. PLOTTING
print("\n20. PLOTTING")
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('TEST PLOT')
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.show()

