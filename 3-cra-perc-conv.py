import pandas as pd

# Define the file path
input_file_path = '/Users/femisokoya/Documents/GitHub/3-cra/melted1_results.csv'
output_file_path = '/Users/femisokoya/Documents/GitHub/3-cra/3-cra-convert.csv'

# Read the CSV file
df = pd.read_csv(input_file_path)

# List of columns to convert to 2 decimal point
columns_to_convert = [
    'Value'
]

# Convert Value columns to 2 decimal point floats
df[columns_to_convert] = df[columns_to_convert].round(2).astype(float)

# convert the year column
df['Year'] = df['Year'].str.replace(r'-(\d{2})$', r'-20\1', regex=True)

# Save the result to a new CSV file
df.to_csv(output_file_path, index=False)