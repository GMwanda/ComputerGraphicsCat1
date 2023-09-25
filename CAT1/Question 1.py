import json
import pandas as pd
import os

# Directory containing JSONL files
jsonl_directory = '/School Stuuf/3.2 Notes/AI/PythonCodeLabs/CAT1/data/'

# Dictionary to store data for each language
language_data = {}

# Iterate over the JSONL files
for filename in os.listdir(jsonl_directory):
    if filename.endswith(".jsonl"):
        file_path = os.path.join(jsonl_directory, filename)

        # Extract language code from the filename, assuming the format is en-xx.jsonl
        language_code = filename.split('.')[0]

        # Initialize language-specific data dictionary
        if language_code not in language_data:
            language_data[language_code] = []

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Load JSON data from each line
                    data = json.loads(line)
                    language_data[language_code].append(data)
                except json.JSONDecodeError:
                    # Handle invalid JSON lines (skip or log as needed)
                    print(f"Skipping invalid JSON line in {filename}: {line}")

# Iterate over language data and create DataFrames
for language_code, data in language_data.items():
    # Create a DataFrame for the language
    df = pd.DataFrame(data, columns=['id', 'utt', 'annot_utt'])

    # Define Excel filename using language code
    excel_filename = f'{language_code}.xlsx'

    # Export DataFrame to Excel
    df.to_excel(excel_filename, index=False)

