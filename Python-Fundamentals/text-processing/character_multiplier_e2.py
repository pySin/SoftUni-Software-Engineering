# Character Multiplier

def string_longer(string_1, string_2):
    if len(string_1) >= len(string_2):
        longest_string = string_1
    else:
        longest_string = string_2
    return longest_string


def multiplied_codes(string_1, string_2):
    longest_string = string_longer(string_1, string_2)
    total_sum = 0

    for i in range(len(longest_string)):
        if i > len(string_1) - 1 or i > len(string_2) - 1:
            total_sum += ord(longest_string[i])
        else:
            total_sum += ord(string_1[i]) * ord(string_2[i])
    return total_sum


if __name__ == "__main__":
    two_strings = input().split()
    # print(two_strings)
    print(multiplied_codes(two_strings[0], two_strings[1]))
