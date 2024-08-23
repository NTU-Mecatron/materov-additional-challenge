import pandas as pd
import xlsxwriter

def convert_spreadsheet(csv_file_path: str) -> None:
    '''
    Utility function to convert a CSV file to an XLSX file with rearranged columns. 

    It will produce a new file with the same name as the input file, but with an XLSX extension.'''

    df = pd.read_csv(csv_file_path)
    new_df = pd.DataFrame()

    # Map the columns to the format required
    column_mapping = {
        'time_elapsed': 'Time Elapsed (s)',
        'frame_number': 'Current Frame',
        'x_min': 'X Bound, Left',
        'x_max': 'X Bound, Right',
        'y_min': 'Y Bound, Upper',
        'y_max': 'Y Bound, Lower',
    }

    # Map and rename columns from the original DataFrame to the new DataFrame
    for old_col, new_col in column_mapping.items():
        if old_col in df.columns:
            new_df[new_col] = df[old_col]

    # Write the rearranged data to an XLS file
    xls_file_path = csv_file_path.replace('.csv', '.xlsx')
    new_df.to_excel(xls_file_path, index=False, engine='xlsxwriter')

    print(f"Rearranged columns saved to {xls_file_path}")