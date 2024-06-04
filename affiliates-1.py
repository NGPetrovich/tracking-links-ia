import pandas as pd
import glob
import os

list_of_files = glob.glob(os.path.join('extract-here', '*.csv'))
if not list_of_files:
    raise FileNotFoundError("No CSV files found in the 'extract-here' directory.")
file_path = list_of_files[0]

df = pd.read_csv(file_path)

# Step 1: Some tracking links do not have Site Name
df['Site Name'] = df['Site Name'].fillna(df['Creative Name'])

# Step 2: Keep only relevant columns
df = df[['Affiliate ID', 'Site ID', 'Username', 'Site Name', 'Clicks', 'Registrations', 'First Deposit Count', 'Deposits', 'Total Commission']]

# Step 3: Sort lines to make sure that each affiliate data can be summed
df = df.sort_values(by=['Affiliate ID', 'Site ID'])

# Step 4: Delete automatically generated grand total line
df = df[df['Username'].notna()]

print(df)
output_path = './processed_data.csv'
df.to_csv(output_path, index=False)
