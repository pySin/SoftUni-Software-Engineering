# Replace repeating chars


def repeating_chars(sequence):
    sequence_list = [x for x in sequence]
    for i in range(len(sequence) - 1, -1, -1):
        if i == 0:
            continue

        if sequence_list[i] == sequence_list[i - 1]:
            sequence_list.pop(i)
    return sequence_list


if __name__ == "__main__":
    row = input()
    unique_chars = repeating_chars(row)
    print(f"{''.join(unique_chars)}")
