# Repeat String

def repeat_length(word):
    return word * len(word)


if __name__ == "__main__":
    words = input().split()
    for one_word in words:
        print(repeat_length(one_word), end="")
