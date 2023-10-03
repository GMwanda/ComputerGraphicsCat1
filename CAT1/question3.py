import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
english_train_file_path = os.path.join(current_directory, 'eng-train.jsonl')
german_train_file_path = os.path.join(current_directory, 'ger-train.jsonl')
swahili_train_file_path = os.path.join(current_directory, 'swa-train.jsonl')
output_file_path = os.path.join(current_directory, 'translations.json')
english_train_data = []
german_train_data = []
swahili_train_data = []

with open(english_train_file_path, 'r') as eng_train_file:
    for line in eng_train_file:
        data = json.loads(line)
        english_train_data.append(data)

with open(german_train_file_path, 'r') as ger_train_file:
    for line in ger_train_file:
        data = json.loads(line)
        german_train_data.append(data)

with open(swahili_train_file_path, 'r') as swa_train_file:
    for line in swa_train_file:
        data = json.loads(line)
        swahili_train_data.append(data)

translations = []
for eng_data, ger_data, swa_data in zip(english_train_data, german_train_data, swahili_train_data):
    eng_utt = eng_data.get("utt")
    ger_utt = ger_data.get("utt")
    swa_utt = swa_data.get("utt")
    translation_entry = {
        "id": eng_data.get("id"),
        "en": eng_utt,
        "ger": ger_utt,
        "swa": swa_utt,
    }
    translations.append(translation_entry)

translations_json = {"translations": translations}
with open(output_file_path, "w", encoding="utf-8") as json_file:
    json.dump(translations_json, json_file, ensure_ascii=False, indent=4)
print(f"Translations saved to '{output_file_path}'")
