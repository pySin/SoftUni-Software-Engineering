# Reverse String


def reverse_text(text: str):
    start = len(text) - 1
    end = 0

    while start >= end:
        yield text[start]
        start -= 1


for char in reverse_text("step"):
    print(char, end='')
