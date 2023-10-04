import json
import os

from Constraints import ENGLISH_TEST_OUTPUT, ENGLISH_TRAIN_OUTPUT, ENGLISH_DEV_OUTPUT, GERMAN_TEST_OUTPUT, \
    GERMAN_TRAIN_OUTPUT, GERMAN_DEV_OUTPUT, KISWAHILI_TEST_OUTPUT, KISWAHILI_TRAIN_OUTPUT, KISWAHILI_DEV_OUTPUT


def read_jsonl_file(file_path):
    with open(file_path, 'r') as jsonl_file:
        return [json.loads(line) for line in jsonl_file]


def write_to_output_file(data_list, output_path):
    with open(output_path, 'a') as output_file:
        for record in data_list:
            json.dump(record, output_file)
            output_file.write('\n')


def get_output_paths(partition):
    return {
        "test": (ENGLISH_TEST_OUTPUT, GERMAN_TEST_OUTPUT, KISWAHILI_TEST_OUTPUT),
        "train": (ENGLISH_TRAIN_OUTPUT, GERMAN_TRAIN_OUTPUT, KISWAHILI_TRAIN_OUTPUT),
        "dev": (ENGLISH_DEV_OUTPUT, GERMAN_DEV_OUTPUT, KISWAHILI_DEV_OUTPUT)
    }


def partition_language():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(current_directory, 'data')
    file_list = ["en-US.jsonl", "de-DE.jsonl", "sw-KE.jsonl"]

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            data_list = read_jsonl_file(file_path)
            partition = data_list[0].get("partition")

            output_paths = get_output_paths(partition)
            output_path = output_paths[file_list.index(file_name)]

            write_to_output_file(data_list, os.path.join(current_directory, output_path))

partition_language()
