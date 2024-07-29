import pandas as pd
import os

def combine_excel_files(folder_path):
    # List to hold dataframes
    df_list = []
    print(folder_path)
    print(os.listdir(folder_path))

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        print(filename)
        
        # Construct full file path
        file_path = os.path.join(folder_path, filename)
        print(file_path)
        # Read the Excel file
        df = pd.read_excel(file_path)
        print("okok")
        # Add a column for the file name
        df['FileName'] = filename

        # Append the dataframe to the list
        df_list.append(df)

    # Concatenate all dataframes
    combined_df = pd.concat(df_list, ignore_index=True, sort=False)

    return combined_df

# Specify the folder path containing the Excel files
folder_path = 'excel_files'
print(folder_path)

# Combine the Excel files
combined_df = combine_excel_files(folder_path)

# Save the combined dataframe to a new Excel file
output_path = 'resultfile/combined_output.xlsx'
print(combined_df)
combined_df.to_excel(output_path, index=False)

