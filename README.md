# WordTally

WordTally is a Python script that allows you to analyze text files and generate word frequency statistics. 

## Features

- Count the occurrences of individual words in a text file.
- Exclude specified words from the analysis.
- Customize the number of most repeated words to display.
- Option to show the percentage of each word in relation to the total number of words.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

```bash
git clone https://github.com/RemmyNine/WordTally.git

2. Navigate to the project directory:
cd wordTotally

## Usage
python wordtally.py -l <file_path> [-e <exclude_words>] [-t <top_words>] [-p]

Options
-e <exclude_words> or --exclude <exclude_words>: Specify words to exclude from the analysis. Separate multiple words with spaces.
-t <top_words> or --top <top_words>: Set the number of most repeated words to display. Default value is 5 if not specified.
-p or --percentage: Show the percentage of each word in relation to the total number of words.

Example
 python wordtally.py -l sample.txt -e the and -t 10 -p
