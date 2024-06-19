import pandas as pd

# Load the first CSV file
df1 = pd.read_csv('buffer.csv')

# Load the second CSV file
df2 = pd.read_csv('metrics.csv')

# Extract the 4th column from the second CSV file (index 3)
# Adjust this index if your CSV file has a header row or different column ordering
fourth_column = df2.iloc[:, 3]

# Add the extracted column to the first dataframe
df1['ln_sim_ass_4'] = fourth_column

# Save the result to a new CSV file
df1.to_csv('combined_file.csv', index=False)

