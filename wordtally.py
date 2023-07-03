#!/usr/bin/env python3

import argparse
from collections import Counter
import sys
import re


def analyze_text(text, exclude_list, show_top, show_percentage, min_length, max_length, output=None):

    # Split the text into words based on separators
    words = re.split(r"[.,\-\s]+", text)

    # Exclude specified words
    filtered_words = [word for word in words if word.lower() not in exclude_list and min_length <= len(word) <= max_length]

    # Count the occurrence of each word
    word_count = Counter(filtered_words)

    # Find the most repeated words
    most_common_words = word_count.most_common(show_top)

    total_words = sum(word_count.values())

    final_words = []

    print(f"The {show_top} most repeated words:")
    for word, count in most_common_words:
        percentage = (count / total_words) * 100
        print(f"'{word}': {count} ({percentage:.2f}%)" if show_percentage else f"'{word}': {count}")
        final_words.append(word)

    if output:
        try:
            with open(output, "w") as file:
                file.write("\n".join(final_words))
            print(f"Output saved to {output}.")
        except IOError:
            print("Error writing to the output file.")
            return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a text file and find the most repeated words.")
    parser.add_argument("-l", "--file-path", help="Path to the text file")
    parser.add_argument("-e", "--exclude", nargs="*", default=[], help="Words to exclude from analysis")
    parser.add_argument("-t", "--top", type=int, default=5, help="Number of most repeated words to show")
    parser.add_argument("-p", "--percentage", action="store_true", help="Show the percentage of each word")
    parser.add_argument("--min-length", type=int, default=0, help="Minimum length of words to include")
    parser.add_argument("--max-length", type=int, default=float('inf'), help="Maximum length of words to include")
    parser.add_argument("-o", "--output", help="Save output to file")
    args = parser.parse_args()

    text = ""

    if args.file_path is not None:
        try:
            with open(file_path, "r") as file:
                text = file.read()
        except FileNotFoundError:
            print("File not found.")
            exit()
    else:
        if sys.stdin.isatty():
            print("stdin is empty")
            exit()
        else:
            text = sys.stdin.read()


    analyze_text(text, args.exclude, args.top, args.percentage, args.min_length, args.max_length, args.output)
