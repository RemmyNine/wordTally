import argparse
from collections import Counter
import re

def analyze_text(file_path, exclude_list, show_top, show_percentage):
    try:
        with open(file_path, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found.")
        return

    # Split the text into words based on separators
    words = re.split(r"[.,\-\s]+", text)

    # Exclude specified words
    filtered_words = [word for word in words if word.lower() not in exclude_list]

    # Count the occurrence of each word
    word_count = Counter(filtered_words)

    # Find the most repeated words
    most_common_words = word_count.most_common(show_top)

    total_words = sum(word_count.values())

    print(f"The {show_top} most repeated words:")
    for word, count in most_common_words:
        percentage = (count / total_words) * 100
        print(f"'{word}': {count} ({percentage:.2f}%)" if show_percentage else f"'{word}': {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a text file and find the most repeated words.")
    parser.add_argument("-l", "--file-path", required=True, help="Path to the text file")
    parser.add_argument("-e", "--exclude", nargs="*", default=[], help="Words to exclude from analysis")
    parser.add_argument("-t", "--top", type=int, default=5, help="Number of most repeated words to show")
    parser.add_argument("-p", "--percentage", action="store_true", help="Show the percentage of each word")
    args = parser.parse_args()

    analyze_text(args.file_path, args.exclude, args.top, args.percentage)
