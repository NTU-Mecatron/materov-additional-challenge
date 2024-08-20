import pandas as pd
import xlsxwriter

# Read the CSV file
csv_file_path = 'spreadsheet.csv'
df = pd.read_csv(csv_file_path)

# Print out the columns in the CSV file
print("Columns in the CSV file:")
print(df.columns.tolist())

# # Rearrange the columns as needed
# # Example: rearrange columns in reverse order
# rearranged_columns = df.columns.tolist()[::-1]
# df_rearranged = df[rearranged_columns]

new_df = pd.DataFrame()

column_mapping = {
    'frame_number': 'Current Frame',
    'x_min': 'X Bound, Left',
    'x_max': 'X Bound, Right',
    'y_min': 'Y Bound, Upper',
    'y_max': 'Y Bound, Lower',
}

for old_col, new_col in column_mapping.items():
    if old_col in df.columns:
        new_df[new_col] = df[old_col]

# Write the rearranged data to an XLS file
xls_file_path = 'spreadsheet.xlsx'
new_df.to_excel(xls_file_path, index=False, engine='xlsxwriter')

print(f"Rearranged columns saved to {xls_file_path}")