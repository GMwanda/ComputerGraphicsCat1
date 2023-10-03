
# Revisiting Python README

## Introduction
This project aims to set up a Python3 development environment for the assessment, perform various tasks related to data processing, and provide documentation on the approach taken and collaboration within the team.

## Question 1 - Python3 Development Environment (10 Marks)
In this section, we describe how we set up the Python3 development environment, installed relevant dependencies, and processed the MASSIVE Dataset.

### Environment Setup
We created a Python3 development environment for this assessment, ensuring that all required dependencies were installed. We recommend using PyCharm as our IDE for this project.

### Importing the MASSIVE Dataset
We imported the MASSIVE Dataset mentioned in the Data File above into our development environment.

### Generating en-xx.xlxs Files
Our task was to generate en-xx.xlxs files for all languages in the dataset, with English (en) as the pivot language. We achieved this without using recursive algorithms to avoid inefficient memory usage.

### Flags for Running
To facilitate running this process, we utilized flags in our generator.sh files.

## Question 2 - Working with Files (10 Marks)
This section outlines how we worked with files, including generating separate JSONL files for specific languages and creating a large JSON file for all translations from English to other languages.

### Generating JSONL Files
For English (en), Swahili (sw), and German (de), we generated separate JSONL files for test, train, and dev data sets.

### Large JSON File
We also created a large JSON file containing all translations from English (en) to other languages (xx) while including the id and utt for all the train sets. We ensured that the JSON file structure was prettily printed for better readability.
For further details and code walkthrough, please refer to the relevant sections in our GitHub repository.

---
