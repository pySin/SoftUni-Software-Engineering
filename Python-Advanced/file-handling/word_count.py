# Word Count


def read_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        r_file = f.read()
    return r_file


def acquire_text(file_name: str) -> list:
    acquired_text = [x.strip("-.?,") for x in read_file(file_name).lower().split()]
    return acquired_text


def word_count(words_to_check: list, text: list) -> dict:
    words_count = {}
    for word in words_to_check:
        words_count[word] = text.count(word)
    return words_count


def sort_words(words_count: dict) -> list:
    sorted_words_count = sorted(words_count.items(), key=lambda x: -x[1])
    return sorted_words_count


def display_words(sorted_words_count: list):
    for word_counted in sorted_words_count:
        print(f"{word_counted[0]} - {word_counted[1]}")


def call_functions():
    words_to_check = read_file("words.txt").split()
    acquired_text = acquire_text("input.txt")
    words_count = word_count(words_to_check, acquired_text)
    sorted_words_count = sort_words(words_count)
    display_words(sorted_words_count)


if __name__ == "__main__":
    call_functions()
