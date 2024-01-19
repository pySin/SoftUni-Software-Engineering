# Vowels Ratio
import re


def open_files(filename):
    open_file = open(filename, "r", encoding="utf8")
    return open_file


def find_words(open_file):
    all_words = []
    for line in open_file:
        pattern = "[\w’]+"
        line_words = re.findall(pattern, line)
        all_words.extend(line_words)
    return all_words


def words_with_ratio(one_word):
    vowels = 0
    for letter in one_word:
        if letter in "aeoiuyAEOIUY":
            vowels += 1

    if "’" in one_word:
        ratio = (vowels / (len(one_word) - 1)) * 100
        return [one_word, round(ratio, 2)]

    ratio = (vowels / len(one_word)) * 100
    return [one_word, round(ratio, 2)]


def sort_by_ratio(one_word):
    return one_word[1]


def function_call():
    filename = "story.txt"
    opened_file = open_files(filename)
    words = find_words(opened_file)
    words_ratios = list(map(words_with_ratio, words))
    words_ratios.sort(key=sort_by_ratio)
    filtered_ratios = list(filter(lambda x: x[0] if "’" in x[0] else None, words_ratios))
    apostrophe_ratio = (len(filtered_ratios) / len(words_ratios)) * 100
    print(f"The words with apostrophe are {apostrophe_ratio:.2f} of all words.")


if __name__ == "__main__":
    function_call()
