import json
import pandas as pd

# List of JSON file names
json_files = ['af-ZA.jsonl']

# Create an empty list to store DataFrames
dataframes = []

# Iterate over each JSON file
for json_file in json_files:
    with open(json_file, 'r') as file:
        # Load JSON data into a Python dictionary or list
        data = json.load(file)

        # Convert JSON data to a DataFrame
        df = pd.DataFrame(data)

        # Append the DataFrame to the list
        dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame (if needed)
# This step is optional and depends on your specific requirements.
combined_df = pd.concat(dataframes, ignore_index=True)

# Export each DataFrame to an Excel file
for i, df in enumerate(dataframes):
    excel_filename = f'output_data_{i + 1}.xlsx'
    df.to_excel(excel_filename, index=False)

# Optionally, export the combined DataFrame to a single Excel file
# combined_df.to_excel('combined_output_data.xlsx', index=False)