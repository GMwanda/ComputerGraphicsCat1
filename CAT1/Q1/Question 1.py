import argparse
import json
import os
from pathlib import Path

import pandas as pd


def get_script_directory():
    # Get the directory where this script is located
    script_path = Path(__file__).resolve()
    return script_path.parent


def extract_data_from_jsonl(jsonl_directory):
    language_data = {}

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

    return language_data


def create_and_export_excel_files(language_data, output_directory):
    for language_code, data in language_data.items():
        # Create a DataFrame for the language with the specified columns
        df = pd.DataFrame(data, columns=['id', 'utt', 'annot_utt'])

        # Define Excel filename using language code
        excel_filename = f'{language_code}.xlsx'

        # Export DataFrame to Excel
        excel_path = os.path.join(output_directory, excel_filename)
        df.to_excel(excel_path, index=False)


def main():
    # Replace the JSONL and output directories with the provided path
    jsonl_directory = r'S:\School Stuuf\3.2 Notes\ComputerGraphics\ClassProjectCodes\CAT1\data'
    output_directory = get_script_directory()  # You can change this to the desired output directory

    # Extract data from JSONL files
    language_data = extract_data_from_jsonl(jsonl_directory)

    # Create and export Excel files
    create_and_export_excel_files(language_data, output_directory)


if __name__ == "__main__":
    main()
