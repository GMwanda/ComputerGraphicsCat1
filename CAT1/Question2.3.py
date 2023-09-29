import json
import os
import glob

# Find all "en-US.jsonl" files in the current directory.
input_files = glob.glob("*-US.jsonl")

# Define the output JSON file.
output_json_file = "translations.json"

# Initialize an empty list to store translations.
translations = []

# Loop through each found file.
for input_file in input_files:
    with open(input_file, "r") as file:
        # Read each line in the JSONL file.
        for line in file:
            data = json.loads(line)

            # Check if the locale is "en" and add the "id" and "utt" to the translations list.
            if data.get("locale") == "en":
                translation = {"id": data.get("id"), "utt": data.get("utt")}
                translations.append(translation)

# Create the final JSON structure.
output_data = {"translations": translations}

# Write the JSON data to the output file with pretty-printing.
with open(output_json_file, "w", encoding="utf-8") as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)

print(f"Translations saved to {output_json_file}")
