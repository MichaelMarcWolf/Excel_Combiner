import pandas as pd
import os

def combine_excel_files(folder_path):
    # List to hold dataframes
    df_list = []
    print(folder_path)

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        
        # Construct full file path
        file_path = os.path.join(folder_path, filename)
        print(file_path)
        # Read the Excel file
        try:
            df = pd.read_excel(file_path, engine='openpyxl')
        except:
            try: 
                df = pd.read_excel(file_path, engine='xlrd')
            except: 
                print("Not imported: " + filename)
        # Add a column for the file name
        df['FileName'] = filename

        # Append the dataframe to the list
        df_list.append(df)

    # Concatenate all dataframes
    combined_df = pd.concat(df_list, ignore_index=True, sort=False)

    return combined_df