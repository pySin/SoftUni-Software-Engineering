# Replace repeating chars 2


def remove_repetitions(sequence):
    new_sequence = ""
    for i in range(len(sequence)):
        if i == 0:
            continue

        if sequence[i] != sequence[i - 1]:
            new_sequence += sequence[i - 1]

        if i == len(sequence) - 1:
            new_sequence += sequence[i]

    return new_sequence


if __name__ == "__main__":
    char_sequence = input()
    remove_repetitions(char_sequence)
