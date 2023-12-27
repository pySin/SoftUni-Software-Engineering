# Text Filter


def banned_words(text, forbidden_words):
    banned = forbidden_words.split(", ")
    for word in banned:

        text = text.replace(word, len(word) * "*")
    return text


if __name__ == "__main__":
    no_words = input()
    description = input()
    print(banned_words(description, no_words))
