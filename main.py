import pandas as pd
import os
from excel_combine import  combine_excel_files

# Specify the folder path containing the Excel files
folder_path = 'excel_files'
#folder_path = 'test_files'
print(folder_path)

# Combine the Excel files
combined_df = combine_excel_files(folder_path)

# Save the combined dataframe to a new Excel file
output_path = 'resultfile/combined_output.xlsx'
print(combined_df)
combined_df.to_excel(output_path, index=False)

