# Extract Person Information


n = int(input())

for _ in range(n):
    phrase = input()
    indexes = []

    for letter in phrase:
        if letter == "@":
            indexes.insert(0, phrase.index(letter))
        elif letter == "|":
            indexes.insert(1, phrase.index(letter))
        elif letter == "#":
            indexes.append(phrase.index(letter))
        elif letter == "*":
            indexes.append(phrase.index(letter))
    print(f"{phrase[indexes[0] + 1: indexes[1]]} is {phrase[indexes[2] + 1: indexes[3]]} years old.")
