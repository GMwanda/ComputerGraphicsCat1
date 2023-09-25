import os
import pandas as pd
import Constraints
import json

folder_path = '/Users/dave/PycharmProjects/compGraphicsClass/CAT1/data'
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

# print(file_list)
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path) and file_name == 'en-US.jsonl':
        # print(file_path)
        with open(file_path, 'r') as jsonl_file:
            # df = json.load(file)
            for line in jsonl_file:
                data = json.loads(line)
                partition = data.get("partition")  # Access the "Partition" attribute
                if partition == "test":
                    # print(data)
                    engtest.append(data)
                elif partition == "train":
                    engtrain.append(data)
                else:
                    engdev.append(data)
            # print('test')
            # print(engtest)
            with open(Constraints.ENGLISH_TEST_OUTPUT, 'a') as testfile:
                for record in engtest:
                    json.dump(record, testfile)
                    testfile.write('\n')
            # print('train')
            # print(engtrain)
            with open(Constraints.ENGLISH_TRAIN_OUTPUT, 'a') as trainfile:
                for t in engtrain:
                    json.dump(t, trainfile)
                    trainfile.write('\n')
            # print('dev')
            # print(engdev)
            with open(Constraints.ENGLISH_DEV_OUTPUT, 'a') as devfile:
                for t in engdev:
                    json.dump(t, devfile)
                    devfile.write('\n')
    elif os.path.isfile(file_path) and file_name == 'de-DE.jsonl':
        with open(file_path, 'r') as jsonl_file:
            # df = json.load(file)
            for line in jsonl_file:
                data = json.loads(line)
                partition = data.get("partition")  # Access the "Partition" attribute
                if partition == "test":
                    # print(data)
                    gertest.append(data)
                elif partition == "train":
                    gertrain.append(data)
                else:
                    gerdev.append(data)
            # print('test')
            # print(engtest)
            with open(Constraints.GERMAN_TEST_OUTPUT, 'a') as testfile:
                for record in gertest:
                    json.dump(record, testfile)
                    testfile.write('\n')
            # print('train')
            # print(engtrain)
            with open(Constraints.GERMAN_TRAIN_OUTPUT, 'a') as trainfile:
                for t in gertrain:
                    json.dump(t, trainfile)
                    trainfile.write('\n')
            # print('dev')
            # print(engdev)
            with open(Constraints.GERMAN_DEV_OUTPUT, 'a') as devfile:
                for t in gerdev:
                    json.dump(t, devfile)
                    devfile.write('\n')
    else:
        with open(file_path, 'r') as jsonl_file:
            # df = json.load(file)
            for line in jsonl_file:
                data = json.loads(line)
                partition = data.get("partition")  # Access the "Partition" attribute
                if partition == "test":
                    # print(data)
                    swatest.append(data)
                elif partition == "train":
                    swatrain.append(data)
                else:
                    swadev.append(data)
            # print('test')
            # print(engtest)
            with open(Constraints.KISWAHILI_TEST_OUTPUT, 'a') as testfile:
                for record in swatest:
                    json.dump(record, testfile)
                    testfile.write('\n')
            # print('train')
            # print(engtrain)
            with open(Constraints.KISWAHILI_TRAIN_OUTPUT, 'a') as trainfile:
                for t in swatrain:
                    json.dump(t, trainfile)
                    trainfile.write('\n')
            # print('dev')
            # print(engdev)
            with open(Constraints.KISWAHILI_DEV_OUTPUT, 'a') as devfile:
                for t in swadev:
                    json.dump(t, devfile)
                    devfile.write('\n')



