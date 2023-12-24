# Rage Quit


def unique_symbols(sequence):
    unique_row = ""
    for char in sequence:
        if char.isdigit():
            continue
        if char.upper() not in unique_row:
            unique_row += char.upper()
    return len(unique_row)


def rage(sequence):
    new_sequence = ""
    sequence_to_multiply = ""
    multiplications = ""

    for i in range(len(sequence)):
        if not sequence[i].isdigit():
            sequence_to_multiply += sequence[i]
        elif sequence[i].isdigit():
            # print(f"some: {multiplications}")
            multiplications += sequence[i]
            if i == len(sequence) - 1:
                new_sequence += int(multiplications) * sequence_to_multiply
                break
            elif sequence[i + 1].isdigit():
                continue
            else:
                # print(sequence_to_multiply)
                new_sequence += int(multiplications) * sequence_to_multiply
                sequence_to_multiply = ""
                multiplications = ""

    # print(new_sequence)
    return new_sequence.upper()


if __name__ == "__main__":
    row = input()
    print(f"Unique symbols used: {unique_symbols(row)}")
    print(rage(row))
