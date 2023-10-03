import json
import os
from pathlib import Path

import pandas as pd


def get_script_directory():
    # Get the directory where this script is located
    script_path = Path(__file__).resolve()
    return script_path.parent


def create_excel_sheets_directory():
    # Get the directory where this script is located
    script_path = Path(__file__).resolve()

    # Create a subdirectory called "ExcelSheets1" in the script's directory
    excel_sheets_directory = script_path.parent / "ExcelSheets1"
    os.makedirs(excel_sheets_directory, exist_ok=True)  # Ensure it's created if it doesn't exist

    return excel_sheets_directory


def find_jsonl_files(jsonl_directory):
    # Use a list comprehension to find JSONL files
    jsonl_files = [os.path.join(jsonl_directory, filename) for filename in os.listdir(jsonl_directory) if
                   filename.endswith(".jsonl") and os.path.isfile(os.path.join(jsonl_directory, filename))]

    return jsonl_files

def extract_data_from_jsonl(jsonl_file):
    language_data = []

    with open(jsonl_file, 'r', encoding='utf-8') as file:
        try:
            for line in file:
                # Load JSON data from each line
                data = json.loads(line)
                language_data.append(data)
        except json.JSONDecodeError:
            # Handle invalid JSON lines (skip or log as needed)
            print(f"Skipping invalid JSON line in {jsonl_file}")

    return language_data


def create_and_export_excel_file(jsonl_file, excel_sheets_directory):
    # Extract data from JSONL file
    language_data = extract_data_from_jsonl(jsonl_file)

    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(jsonl_file))[0]

    # Create a DataFrame for the language with the specified columns
    df = pd.DataFrame(language_data, columns=['id', 'utt', 'annot_utt'])

    # Define Excel filename using the file name
    excel_filename = f'{file_name}.xlsx'

    # Define the full path to the Excel file in the "ExcelSheets1" directory
    excel_file_path = os.path.join(excel_sheets_directory, excel_filename)

    # Export DataFrame to Excel
    df.to_excel(excel_file_path, index=False)


def main():
    # Get the script's directory
    jsonl_directory = get_script_directory()

    # Create "ExcelSheets1" directory in the script's directory
    excel_sheets_directory = create_excel_sheets_directory()

    # Find all JSONL files in the specified directory
    jsonl_files = find_jsonl_files(jsonl_directory)

    # Process each JSONL file and create Excel files in the "ExcelSheets1" directory
    for jsonl_file in jsonl_files:
        create_and_export_excel_file(jsonl_file, excel_sheets_directory)

if __name__ == "__main__":
    main()
