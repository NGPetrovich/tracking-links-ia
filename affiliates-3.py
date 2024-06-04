import pandas as pd
import pickle

# Importing shared variable
with open('variable.pkl', 'rb') as file:
    internal_affiliate_id = pickle.load(file)

file_path = './subtotals_part_1.csv'
df = pd.read_csv(file_path)

# Function to calculate subtotals for each Site ID and insert them
def insert_subtotals(df):
    result = pd.DataFrame()
    for username, group in df.groupby('Username'):
        subtotal = group.sum(numeric_only=True)
        subtotal['Username'] = 'Subtotal'
        subtotal['Affiliate ID'] = group['Affiliate ID'].iloc[0]  # Use the first Affiliate ID in the group
        subtotal['Site ID'] = group['Site ID'].iloc[-1]  # Use the last Site ID in the group
        subtotal['Site Name'] = username
        result = pd.concat([result, group, subtotal.to_frame().T], ignore_index=True)
    return result

# Step 1: Select dataframe of all non-MB websites
external_data = df[df['Affiliate ID'] != internal_affiliate_id]

# Step 2: Apply the function to all non-MB websites
result_with_subtotals = insert_subtotals(external_data).reset_index(drop=True)

# Step 3: Combine non-MB websites dataframe with internal dataframe
combined_data = pd.concat([result_with_subtotals, df[df['Affiliate ID'] == internal_affiliate_id]], ignore_index=True)

# Step 4: Sort the final DataFrame by Site ID and then by Affiliate ID
final_sorted_data = combined_data.sort_values(by=['Affiliate ID', 'Site ID']).reset_index(drop=True)

output_path = './subtotals_part_2.csv'
final_sorted_data.to_csv(output_path, index=False)

print("Processed data saved to", output_path)
