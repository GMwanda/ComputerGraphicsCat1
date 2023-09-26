import json
import os
from pathlib import Path
import pandas as pd

def get_script_directory():
    # Get the directory where this script is located
    script_path = Path(__file__).resolve()
    return script_path.parent

def find_jsonl_files(jsonl_directory):
    # Initialize a list to store the paths of JSONL files
    jsonl_files = []

    # List all files in the JSONL directory
    for filename in os.listdir(jsonl_directory):
        file_path = os.path.join(jsonl_directory, filename)

        # Check if the file is a JSONL file (ends with .jsonl)
        if filename.endswith(".jsonl") and os.path.isfile(file_path):
            jsonl_files.append(file_path)

    return jsonl_files

def extract_data_from_jsonl(jsonl_file):
    language_data = []

    with open(jsonl_file, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                # Load JSON data from each line
                data = json.loads(line)
                language_data.append(data)
            except json.JSONDecodeError:
                # Handle invalid JSON lines (skip or log as needed)
                print(f"Skipping invalid JSON line in {jsonl_file}")

    return language_data

def create_and_export_excel_file(jsonl_file, output_directory):
    # Extract data from JSONL file
    language_data = extract_data_from_jsonl(jsonl_file)

    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(jsonl_file))[0]

    # Create a DataFrame for the language with the specified columns
    df = pd.DataFrame(language_data, columns=['id', 'utt', 'annot_utt'])

    # Define Excel filename using the file name
    excel_filename = f'{file_name}.xlsx'

    # Define the full path to the Excel file
    excel_file_path = os.path.join(output_directory, excel_filename)

    # Export DataFrame to Excel
    df.to_excel(excel_file_path, index=False)

def main():
    # Replace the JSONL and output directories with the provided path
    jsonl_directory = get_script_directory()  # You can change this to the desired output directory

    # Find all JSONL files in the specified directory
    jsonl_files = find_jsonl_files(jsonl_directory)

    # Process each JSONL file and create Excel files
    for jsonl_file in jsonl_files:
        create_and_export_excel_file(jsonl_file, jsonl_directory)

if __name__ == "__main__":
    main()
