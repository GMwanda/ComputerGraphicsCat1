import os
import json
import Constraints

def partitionLanguage():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(current_directory, 'data')
    file_list = ["en-US.jsonl", "de-DE.jsonl", "sw-KE.jsonl"]
    engtest = []
    engtrain = []
    engdev = []
    gertest = []
    gertrain = []
    gerdev = []
    swatest = []
    swatrain = []
    swadev = []
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name == 'en-US.jsonl':
            with open(file_path, 'r') as jsonl_file:
                for line in jsonl_file:
                    data = json.loads(line)
                    partition = data.get("partition")
                    if partition == "test":
                        engtest.append(data)
                    elif partition == "train":
                        engtrain.append(data)
                    else:
                        engdev.append(data)

                with open(os.path.join(current_directory, Constraints.ENGLISH_TEST_OUTPUT), 'a') as testfile:
                    for record in engtest:
                        json.dump(record, testfile)
                        testfile.write('\n')

                with open(os.path.join(current_directory, Constraints.ENGLISH_TRAIN_OUTPUT), 'a') as trainfile:
                    for t in engtrain:
                        json.dump(t, trainfile)
                        trainfile.write('\n')

                with open(os.path.join(current_directory, Constraints.ENGLISH_DEV_OUTPUT), 'a') as devfile:
                    for t in engdev:
                        json.dump(t, devfile)
                        devfile.write('\n')
        elif os.path.isfile(file_path) and file_name == 'de-DE.jsonl':
            with open(file_path, 'r') as jsonl_file:
                for line in jsonl_file:
                    data = json.loads(line)
                    partition = data.get("partition")
                    if partition == "test":
                        gertest.append(data)
                    elif partition == "train":
                        gertrain.append(data)
                    else:
                        gerdev.append(data)

                with open(os.path.join(current_directory, Constraints.GERMAN_TEST_OUTPUT), 'a') as testfile:
                    for record in gertest:
                        json.dump(record, testfile)
                        testfile.write('\n')

                with open(os.path.join(current_directory, Constraints.GERMAN_TRAIN_OUTPUT), 'a') as trainfile:
                    for t in gertrain:
                        json.dump(t, trainfile)
                        trainfile.write('\n')

                with open(os.path.join(current_directory, Constraints.GERMAN_DEV_OUTPUT), 'a') as devfile:
                    for t in gerdev:
                        json.dump(t, devfile)
                        devfile.write('\n')
        else:
            with open(file_path, 'r') as jsonl_file:
                for line in jsonl_file:
                    data = json.loads(line)
                    partition = data.get("partition")
                    if partition == "test":
                        swatest.append(data)
                    elif partition == "train":
                        swatrain.append(data)
                    else:
                        swadev.append(data)

                with open(os.path.join(current_directory, Constraints.KISWAHILI_TEST_OUTPUT), 'a') as testfile:
                    for record in swatest:
                        json.dump(record, testfile)
                        testfile.write('\n')

                with open(os.path.join(current_directory, Constraints.KISWAHILI_TRAIN_OUTPUT), 'a') as trainfile:
                    for t in swatrain:
                        json.dump(t, trainfile)
                        trainfile.write('\n')

                with open(os.path.join(current_directory, Constraints.KISWAHILI_DEV_OUTPUT), 'a') as devfile:
                    for t in swadev:
                        json.dump(t, devfile)
                        devfile.write('\n')

