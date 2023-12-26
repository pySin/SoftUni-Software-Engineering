# String explosion


def string_explosion(sequence):
    changed_sequence = ""
    explosions_left = 0

    for i in range(len(sequence)):
        if sequence[i] == ">":
            explosions_left += int(sequence[i + 1])
            changed_sequence += ">"
            continue
        else:
            if explosions_left > 0:
                explosions_left -= 1
                continue
            else:
                changed_sequence += sequence[i]

    return changed_sequence


if __name__ == "__main__":
    char_sequence = input()
    new_sequence = string_explosion(char_sequence)
    print(new_sequence)
