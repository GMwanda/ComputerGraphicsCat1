import json
import os

# Define the path to the directory containing the JSONL files.
data_directory = "data"

# Initialize an empty dictionary to store translations.
translations = {}

# Iterate through each JSONL file in the data directory.
for filename in os.listdir(data_directory):
    if filename.endswith(".jsonl"):
        with open(os.path.join(data_directory, filename), "r", encoding="utf-8") as file:
            # Read each line in the JSONL file.
            for line in file:
                data = json.loads(line)

                # Check if the data is from the train set and the source language is English (en).
                if data.get("partition") == "train" and data.get("locale").startswith("en-"):
                    id = data.get("id")
                    utt = data.get("utt")
                    lang = data.get("locale")[3:]  # Extract the target language (xx).

                    # Check if the language code (xx) already exists in the translations dictionary.
                    if lang not in translations:
                        translations[lang] = []

                    # Append the translation to the corresponding language.
                    translations[lang].append({"id": id, "utt": utt})

# Create the final JSON structure.
output_data = {"translations": translations}

# Write the JSON data to the output file with pretty-printing.
with open("translations.json", "w", encoding="utf-8") as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)

print(f"Translations from English (en) to xx saved to translations.json")
