import json
import os
from pathlib import Path

import pandas as pd


def get_script_directory():
    script_path = Path(__file__).resolve()
    return script_path.parent


def create_excel_sheets_directory():
    script_path = Path(__file__).resolve()
    excel_sheets_directory = script_path.parent / "ExcelSheets1"
    os.makedirs(excel_sheets_directory, exist_ok=True)
    return excel_sheets_directory


def find_jsonl_files(jsonl_directory):
    jsonl_files = [os.path.join(jsonl_directory, filename) for filename in os.listdir(jsonl_directory) if
                   filename.endswith(".jsonl") and os.path.isfile(os.path.join(jsonl_directory, filename))]

    return jsonl_files


def extract_data_from_jsonl(jsonl_file):
    language_data = []

    with open(jsonl_file, 'r', encoding='utf-8') as file:
        try:
            for line in file:
                data = json.loads(line)
                language_data.append(data)
        except json.JSONDecodeError:

            print(f"Skipping invalid JSON line in {jsonl_file}")

    return language_data


def create_and_export_excel_file(jsonl_file, excel_sheets_directory):
    language_data = extract_data_from_jsonl(jsonl_file)
    file_name = os.path.splitext(os.path.basename(jsonl_file))[0]
    df = pd.DataFrame(language_data, columns=['id', 'utt', 'annot_utt'])
    excel_filename = f'{file_name}.xlsx'
    excel_file_path = os.path.join(excel_sheets_directory, excel_filename)
    df.to_excel(excel_file_path, index=False)


def main():
    jsonl_directory = get_script_directory()
    excel_sheets_directory = create_excel_sheets_directory()
    jsonl_files = find_jsonl_files(jsonl_directory)
    for jsonl_file in jsonl_files:
        create_and_export_excel_file(jsonl_file, excel_sheets_directory)


if __name__ == "__main__":
    main()
