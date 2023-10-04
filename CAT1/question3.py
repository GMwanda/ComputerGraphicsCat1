import json
import os


def read_jsonl_file(file_path):
    with open(file_path, 'r') as jsonl_file:
        return [json.loads(line) for line in jsonl_file]


def write_to_output_file(data_list, output_path):
    with open(output_path, 'a') as output_file:
        for record in data_list:
            json.dump(record, output_file)
            output_file.write('\n')


def process_language_files(input_file_paths, output_file_path):
    data_lists = [read_jsonl_file(file_path) for file_path in input_file_paths]

    translations = []
    for entries in zip(*data_lists):
        translation_entry = {
            "id": entries[0].get("id"),
            "en": entries[0].get("utt"),
            "ger": entries[1].get("utt"),
            "swa": entries[2].get("utt"),
        }
        translations.append(translation_entry)

    translations_json = {"translations": translations}
    write_to_output_file([translations_json], output_file_path)


current_directory = os.path.dirname(os.path.abspath(__file__))
input_file_paths = [
    os.path.join(current_directory, 'eng-train.jsonl'),
    os.path.join(current_directory, 'ger-train.jsonl'),
    os.path.join(current_directory, 'swa-train.jsonl')
]
output_file_path = os.path.join(current_directory, 'translations.json')

process_language_files(input_file_paths, output_file_path)
print(f"Translations saved to '{output_file_path}'")
