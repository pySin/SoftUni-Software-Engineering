# Mirror Words
import re


def find_matches(text_string: str) -> list:
    pattern = r"((@|#)([a-zA-Z]{3,})\2\2([a-zA-Z]{3,})\2)"
    matches = re.findall(pattern, text_string)
    return matches


def find_mirror_words(matches: list) -> list:
    mirror_words = []
    for match in matches:
        first_word = match[2]
        second_word = match[3]
        if first_word == second_word[::-1]:
            mirror_words.append([first_word, second_word])
    return mirror_words


def display_findings(mirror_words_data: list, mirror_words: list):
    if len(mirror_words_data) > 0:
        print(f"{len(mirror_words_data)} word pairs found!")
    else:
        print("No word pairs found!")

    words_phrase = ""
    if len(mirror_words) > 0:
        print("The mirror words are:")
        words_phrase = ", ".join([" <=> ".join(word) for word in mirror_words])
    else:
        print("No mirror words!")

    if words_phrase:
        print(words_phrase)


def call_functions():
    text_string = input()

    mirror_words_data = find_matches(text_string)
    mirror_words = find_mirror_words(mirror_words_data)
    display_findings(mirror_words_data, mirror_words)


if __name__ == "__main__":
    call_functions()
