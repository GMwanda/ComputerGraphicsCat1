## Introduction

This project focuses on processing and managing language data. It
answers two main questions:

1. **Python3 Development Environment Setup:** Set up a Python3
development environment, install relevant dependencies, and build a
project structure similar to PyCharm's. Import a massive dataset and
generate language-specific Excel files (en-xx.xlsx) using specific
fields (id, utt, and annot_utt). Recursive algorithms are not used to
optimize performance.

2. **Working with Files:** Generate separate JSONL files for English
(en), Swahili (sw), and German (de) datasets with test, train, and dev
partitions. Create a single large JSON file showcasing translations
from English to other languages (xx) for the training dataset.

## Prerequisites

Before running the project, ensure you have the following
prerequisites installed:

- Python 3.x
- pip (Python package manager)

## Installation

You can install the required Python libraries/packages using the
following command:

```
pip install jsonlines json os pandas sys
```

Project Structure
The project structure should resemble the following:

```
ComputerGraphicsCat1
  └──CAT1
      └──data
      └──Question 1
          └──Question_1.py
      └──Constraints.py
      └──Question2.2.py
      └──Question3.py
      └──README.md
```

The script will generate language-specific Excel files (en-xx.xlsx) in
the results/ directory.
Question 2
Make sure you have the English (en), Swahili (sw), and German (de)
JSONL files (e.g., en-US.jsonl, de-DE.jsonl, sw-KE.jsonl) in the
project directory.

Run the following command to execute Question 2:

```
python q2.py
```
The script will generate separate JSONL files for English, Swahili,
and German in the results/ directory. Additionally, it will create a
large JSON file (translations.json) showcasing translations from
English to other languages.
It appears that you are providing an introduction, prerequisites, installation instructions, project structure, and execution steps for your project. If you want to add a disclaimer section to your project documentation, here's an example of what you could include:

## Disclaimer

The information, data, and code provided in this project are intended for educational and demonstrative purposes only. While we have made efforts to ensure the accuracy and reliability of the content, we make no representations or warranties regarding the completeness, accuracy, or suitability for any purpose.


### Data Privacy

Please be mindful of data privacy and copyright laws when working with datasets and translations. Ensure that you have the appropriate permissions and rights to use and share the data as needed for your specific project.

### Third-Party Dependencies

This project may utilize third-party libraries and tools. Make sure to review and comply with their respective licenses and terms of use. We do not endorse or claim ownership of any third-party software or resources used in this project.

### Changes and Updates

We reserve the right to make changes and updates to this project's code, documentation, and content without prior notice. It is advisable to check for the latest version and updates on our official repository or website.

By using this project, you agree to abide by the terms and conditions outlined in this disclaimer. If you do not agree with these terms, please refrain from using the project.

