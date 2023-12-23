# Emoticon Finder


def emoticon_finder(sentence):
    emoticons = []
    for symbol in range(len(sentence)):
        if sentence[symbol] == ":":
            emoticon = ":" + sentence[symbol + 1]
            emoticons.append(emoticon)
    return emoticons


if __name__ == "__main__":
    phrase = input()
    for emoticon in emoticon_finder(phrase):
        print(emoticon)
