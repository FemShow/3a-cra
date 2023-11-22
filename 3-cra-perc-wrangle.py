import pandas as pd

# Read the Excel file into a DataFrame, skipping the first 4 rows and reading the first 31 rows
percentages_df = pd.read_excel("/Users/femisokoya/Documents/GitHub/CRA/Companies_Register_Activities_2021-22.xls",
                           sheet_name='Table_C1',
                           skiprows=38,
                           nrows=31)

# Melt the DataFrame with 'Corporate body type' as id_vars
melted_df = pd.melt(percentages_df, id_vars=['Corporate body type'], var_name='Year', value_name='Value')

# Create 'Value-obsStatus' column
melted_df['Value-obsStatus'] = ''

# Iterate through each row of the 'Value' column
for index, value in enumerate(melted_df['Value']):
    # Check if the value is an empty string, NaN, or Null
    if pd.isna(value) or value == '':
        melted_df.at[index, 'Value_obsStatus'] = 'z'
    # Check if the value is a hyphen ('-') or (' - ')
    elif isinstance(value, str) and value.strip() in ('-', '- '):
        melted_df.at[index, 'Value'] = '0'

# Save the modified DataFrame to a CSV file
melted_df.to_csv('/Users/femisokoya/Documents/GitHub/3-cra/melted1_results.csv', index=False)

# Print the modified DataFrame to verify the changes
print(melted_df.head())

# Print the modified DataFrame to verify the changes
print(melted_df.head())
