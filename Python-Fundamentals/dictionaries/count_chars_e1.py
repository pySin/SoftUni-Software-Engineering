# Count Chars in Strings


def count_char(sequence):
    occurrences = {}
    for char in sequence:
        if char == " ":
            continue
        else:
            if char in occurrences:
                occurrences[char] += 1
            else:
                occurrences[char] = 1
    return occurrences


if __name__ == "__main__":
    row = input()
    letters_frequency = count_char(row)
    for key, value in letters_frequency.items():
        print(f"{key} -> {value}")
